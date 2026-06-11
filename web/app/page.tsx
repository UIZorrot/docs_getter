'use client';

import { FormEvent, useEffect, useMemo, useState } from 'react';

type Language = 'zh' | 'en';
type JobStatus = 'queued' | 'running' | 'completed' | 'failed' | 'cancelled';

type SkippedEntry = {
    url?: string;
    error?: string;
};

type CrawlJob = {
    job_id: string;
    status: JobStatus;
    start_url: string;
    created_at: string;
    finished_at?: string | null;
    page_count: number;
    skipped_count: number;
    error?: string | null;
    archive_url: string;
    cancel_url: string;
    recent_skipped?: SkippedEntry[];
};

const API_BASE = '/api';
const LANGUAGE_STORAGE_KEY = 'doc-getter-language';
const GITHUB_URL = process.env.NEXT_PUBLIC_GITHUB_URL ?? 'https://github.com';
const TIP_URL =
    process.env.NEXT_PUBLIC_TIP_URL ?? 'https://buy.stripe.com/5kQ4gybHj2T26Rv1Jh2sM00';

const COPY = {
    zh: {
        pageTitle: '抓取文档并下载 ZIP',
        pageDescription: '粘贴文档站 URL，抓取完成后一键下载 Markdown 压缩包。',
        startTitle: '开始抓取',
        urlLabel: '文档 URL',
        submit: '开始抓取并打包 ZIP',
        submitting: '正在提交…',
        cancel: '取消任务',
        resultTitle: '下载结果',
        resultEmpty: '提交任务后会自动更新进度，完成后可在此下载 ZIP。',
        inProgress: '正在抓取并打包，请稍候…',
        downloadZip: '下载 ZIP 压缩包',
        retentionHint: '下载结果为临时文件，服务会按保留策略自动清理。',
        pages: '页面',
        skipped: '跳过',
        createFailed: '创建任务失败',
        pollFailed: '读取任务状态失败',
        cancelFailed: '取消任务失败',
        languageLabel: '语言切换',
        tip: 'Tip',
        skipWarning: '大量页面被跳过，可能是链接解析或权限问题。请检查起始 URL 是否为站点首页。',
        showSkipped: '查看跳过的 URL',
        hideSkipped: '收起',
        waiting: '等待任务开始…',
        github: 'GitHub',
    },
    en: {
        pageTitle: 'Grab docs and download a ZIP',
        pageDescription: 'Paste a docs URL and download the ZIP when the crawl is done.',
        startTitle: 'Start a crawl',
        urlLabel: 'Docs URL',
        submit: 'Start crawling and package ZIP',
        submitting: 'Submitting…',
        cancel: 'Cancel job',
        resultTitle: 'Download result',
        resultEmpty: 'Progress updates automatically after you submit. Download the ZIP here when finished.',
        inProgress: 'Crawling and packaging in progress…',
        downloadZip: 'Download ZIP archive',
        retentionHint: 'Downloads are temporary; old files are cleaned up automatically.',
        pages: 'Pages',
        skipped: 'Skipped',
        createFailed: 'Failed to create the job',
        pollFailed: 'Failed to read job status',
        cancelFailed: 'Failed to cancel the job',
        languageLabel: 'Language',
        tip: 'Tip',
        skipWarning: 'Many pages were skipped — often a bad start URL or link resolution issue. Try the site homepage with a trailing slash.',
        showSkipped: 'Show skipped URLs',
        hideSkipped: 'Hide',
        waiting: 'Waiting for the job to start…',
        github: 'GitHub',
    },
} as const;

const STATUS_LABELS: Record<Language, Record<JobStatus, string>> = {
    zh: {
        queued: '排队中',
        running: '抓取中',
        completed: '已完成',
        failed: '失败',
        cancelled: '已取消',
    },
    en: {
        queued: 'Queued',
        running: 'Running',
        completed: 'Completed',
        failed: 'Failed',
        cancelled: 'Cancelled',
    },
};

function detectPreferredLanguage(): Language {
    if (typeof window === 'undefined') {
        return 'zh';
    }
    const saved = window.localStorage.getItem(LANGUAGE_STORAGE_KEY);
    if (saved === 'zh' || saved === 'en') {
        return saved;
    }
    const browserLanguages = window.navigator.languages?.length
        ? window.navigator.languages
        : [window.navigator.language];
    return browserLanguages.some((value) => value.toLowerCase().startsWith('zh')) ? 'zh' : 'en';
}

function toAbsoluteUrl(apiBase: string, path: string) {
    if (!path) return '';
    if (path.startsWith('http://') || path.startsWith('https://')) return path;
    return `${apiBase}${path}`;
}

function IconArchive() {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" aria-hidden>
            <path d="M4 7h16v12a2 2 0 0 1-2 2H6a2 2 0 0 1-2-2V7Z" />
            <path d="M8 7V5a2 2 0 0 1 2-2h4a2 2 0 0 1 2 2v2" />
            <path d="M12 11v4M10 13h4" />
        </svg>
    );
}

function IconGlobe() {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" aria-hidden>
            <circle cx="12" cy="12" r="9" />
            <path d="M3 12h18M12 3a14 14 0 0 1 0 18M12 3a14 14 0 0 0 0 18" />
        </svg>
    );
}

function IconCheck() {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="2" aria-hidden>
            <path d="M5 12l4 4L19 6" strokeLinecap="round" strokeLinejoin="round" />
        </svg>
    );
}

function IconPlay() {
    return (
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden>
            <path d="M8 5v14l11-7L8 5z" />
        </svg>
    );
}

function IconDownload() {
    return (
        <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" strokeWidth="1.75" aria-hidden>
            <path d="M12 3v12M8 11l4 4 4-4" strokeLinecap="round" strokeLinejoin="round" />
            <path d="M4 19h16" strokeLinecap="round" />
        </svg>
    );
}

function IconGithub() {
    return (
        <svg viewBox="0 0 24 24" fill="currentColor" aria-hidden>
            <path d="M12 2C6.48 2 2 6.58 2 12.26c0 4.5 2.87 8.32 6.84 9.67.5.1.68-.22.68-.48 0-.24-.01-.87-.01-1.7-2.78.62-3.37-1.36-3.37-1.36-.45-1.18-1.12-1.5-1.12-1.5-.92-.65.07-.64.07-.64 1.02.07 1.55 1.06 1.55 1.06.9 1.57 2.36 1.12 2.94.85.09-.67.35-1.12.63-1.38-2.22-.26-4.56-1.14-4.56-5.07 0-1.12.39-2.03 1.03-2.75-.1-.26-.45-1.3.1-2.7 0 0 .84-.27 2.75 1.03A9.2 9.2 0 0 1 12 6.8c.85 0 1.7.11 2.5.33 1.9-1.3 2.74-1.03 2.74-1.03.55 1.4.2 2.44.1 2.7.64.72 1.03 1.63 1.03 2.75 0 3.94-2.34 4.8-4.57 5.06.36.32.68.94.68 1.9 0 1.37-.01 2.47-.01 2.8 0 .27.18.58.69.48A10.03 10.03 0 0 0 22 12.26C22 6.58 17.52 2 12 2z" />
        </svg>
    );
}

export default function HomePage() {
    const [language, setLanguage] = useState<Language>('zh');
    const [startUrl, setStartUrl] = useState('https://openrouter.ai/docs/');
    const [job, setJob] = useState<CrawlJob | null>(null);
    const [submitting, setSubmitting] = useState(false);
    const [error, setError] = useState('');
    const [skippedOpen, setSkippedOpen] = useState(false);

    useEffect(() => {
        setLanguage(detectPreferredLanguage());
    }, []);

    useEffect(() => {
        if (typeof window === 'undefined') return;
        window.localStorage.setItem(LANGUAGE_STORAGE_KEY, language);
        document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    }, [language]);

    const t = COPY[language];
    const statusLabels = STATUS_LABELS[language];

    const isFinished = useMemo(
        () => (job ? ['completed', 'failed', 'cancelled'].includes(job.status) : false),
        [job],
    );

    const isActive = job && (job.status === 'queued' || job.status === 'running');

    const showSkipWarning = useMemo(() => {
        if (!job || job.status !== 'completed') return false;
        return job.skipped_count > 0 && job.skipped_count >= job.page_count;
    }, [job]);

    const progressPercent = useMemo(() => {
        if (!job || job.status === 'queued') return 8;
        if (job.status === 'running') {
            const base = Math.min(90, 12 + job.page_count * 4);
            return Math.max(base, 12);
        }
        if (job.status === 'completed') return 100;
        return 0;
    }, [job]);

    async function refreshJob(jobId: string) {
        const response = await fetch(`${API_BASE}/v1/crawls/${jobId}`, { cache: 'no-store' });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail ?? t.pollFailed);
        }
        setJob(data);
    }

    useEffect(() => {
        if (!job || isFinished) return;
        const timer = window.setInterval(() => {
            refreshJob(job.job_id).catch((cause: unknown) => {
                setError(cause instanceof Error ? cause.message : t.pollFailed);
            });
        }, 2500);
        return () => window.clearInterval(timer);
    }, [isFinished, job, language]);

    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setError('');
        setJob(null);
        setSkippedOpen(false);
        setSubmitting(true);
        try {
            const response = await fetch(`${API_BASE}/v1/crawls`, {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({ start_url: startUrl }),
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail ?? t.createFailed);
            }
            setJob(data);
        } catch (cause: unknown) {
            setError(cause instanceof Error ? cause.message : t.createFailed);
        } finally {
            setSubmitting(false);
        }
    }

    async function handleCancel() {
        if (!job) return;
        setError('');
        try {
            const response = await fetch(toAbsoluteUrl(API_BASE, job.cancel_url), { method: 'POST' });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail ?? t.cancelFailed);
            }
            setJob(data);
        } catch (cause: unknown) {
            setError(cause instanceof Error ? cause.message : t.cancelFailed);
        }
    }

    const resultInnerClass = [
        'cardIconInner',
        job?.status === 'completed' ? 'cardIconInnerSuccess' : '',
        isActive ? 'cardIconInnerRunning' : '',
    ]
        .filter(Boolean)
        .join(' ');

    return (
        <main className="page">
            <header className="header">
                <div className="brand">
                    <p className="brandTitle">txzy/tool/getdoc</p>
                    <a
                        className="tipBtn"
                        href={TIP_URL}
                        target="_blank"
                        rel="noreferrer"
                    >
                        {t.tip}
                    </a>
                </div>
                <div className="langSwitch" role="group" aria-label={t.languageLabel}>
                    <button
                        type="button"
                        className={`langBtn ${language === 'zh' ? 'active' : ''}`}
                        onClick={() => setLanguage('zh')}
                    >
                        中文
                    </button>
                    <button
                        type="button"
                        className={`langBtn ${language === 'en' ? 'active' : ''}`}
                        onClick={() => setLanguage('en')}
                    >
                        EN
                    </button>
                </div>
            </header>

            <div className="pageGrid">
            <section className="card">
                <div className="cardIcon cardIconSquare cardIconRaised" aria-hidden>
                    <IconArchive />
                </div>
                <div className="cardBody">
                    <h1 className="cardTitle">{t.pageTitle}</h1>
                    <p className="cardDesc">{t.pageDescription}</p>
                </div>
            </section>

            <section className="card">
                <div className="cardIcon cardIconRound cardIconInset" aria-hidden>
                    <IconGlobe />
                </div>
                <div className="cardBody">
                    <h2 className="cardTitle">{t.startTitle}</h2>
                    <form className="urlForm" onSubmit={handleSubmit}>
                        <label className="fieldLabel" htmlFor="start-url">
                            {t.urlLabel}
                        </label>
                        <input
                            id="start-url"
                            className="urlInput"
                            required
                            value={startUrl}
                            onChange={(event) => setStartUrl(event.target.value)}
                            placeholder="https://docs.example.com/"
                        />
                        <div className="formActions">
                            <button type="submit" className="btnPrimary" disabled={submitting}>
                                <IconPlay />
                                {submitting ? t.submitting : t.submit}
                            </button>
                            {job && !isFinished ? (
                                <button type="button" className="btnRaised" onClick={handleCancel}>
                                    {t.cancel}
                                </button>
                            ) : null}
                        </div>
                    </form>
                    {error ? <p className="alert alertError">{error}</p> : null}
                </div>
            </section>

            <section className="card">
                <div className="cardIconRing" aria-hidden>
                    <div className={resultInnerClass}>
                        {job?.status === 'completed' ? <IconCheck /> : <IconArchive />}
                    </div>
                </div>
                <div className="cardBody">
                    <h2 className="cardTitle">{t.resultTitle}</h2>

                    {!job ? (
                        <p className="emptyState">{t.resultEmpty}</p>
                    ) : (
                        <>
                            <div className="statsRow">
                                <span className={`badge badge-${job.status}`}>
                                    {statusLabels[job.status]}
                                </span>
                                <span className="statChip">
                                    {t.pages}: <strong>{job.page_count}</strong>
                                </span>
                                <span className="statChip">
                                    {t.skipped}: <strong>{job.skipped_count}</strong>
                                </span>
                            </div>

                            {isActive ? (
                                <div className="statusBar">
                                    <div className="progressTrack">
                                        <div
                                            className={`progressFill ${job.status === 'running' && job.page_count === 0 ? 'progressFillIndeterminate' : ''}`}
                                            style={{ width: `${progressPercent}%` }}
                                        />
                                    </div>
                                    <p className="progressLabel">
                                        {job.status === 'queued' ? t.waiting : t.inProgress}
                                    </p>
                                </div>
                            ) : null}

                            {showSkipWarning ? (
                                <p className="alert alertWarning">{t.skipWarning}</p>
                            ) : null}

                            {job.recent_skipped && job.recent_skipped.length > 0 ? (
                                <>
                                    <button
                                        type="button"
                                        className="btnRaised btnRaisedSmall"
                                        onClick={() => setSkippedOpen((open) => !open)}
                                    >
                                        {skippedOpen ? t.hideSkipped : t.showSkipped} ({job.skipped_count})
                                    </button>
                                    {skippedOpen ? (
                                        <ul className="skippedList">
                                            {job.recent_skipped.map((entry, index) => (
                                                <li key={`${entry.url}-${index}`}>
                                                    {entry.url}
                                                    {entry.error ? <code>{entry.error}</code> : null}
                                                </li>
                                            ))}
                                        </ul>
                                    ) : null}
                                </>
                            ) : null}

                            <div className="formActions" style={{ marginTop: 14 }}>
                                {job.status === 'completed' ? (
                                    <a
                                        className="btnDownload"
                                        href={toAbsoluteUrl(API_BASE, job.archive_url)}
                                        target="_blank"
                                        rel="noreferrer"
                                    >
                                        <IconDownload />
                                        {t.downloadZip}
                                    </a>
                                ) : (
                                    <span className="btnDownload btnDownloadDisabled">
                                        <IconDownload />
                                        {t.downloadZip}
                                    </span>
                                )}
                            </div>

                            {job.status === 'completed' ? (
                                <p className="retentionNote">{t.retentionHint}</p>
                            ) : null}

                            {job.error ? <p className="alert alertError">{job.error}</p> : null}
                        </>
                    )}
                </div>
            </section>

            <footer className="footer">
                <a className="footerBar" href={GITHUB_URL} target="_blank" rel="noreferrer">
                    <span className="footerIcon" aria-hidden>
                        <IconGithub />
                    </span>
                    <span className="footerLabel">{t.github}</span>
                </a>
            </footer>
            </div>
        </main>
    );
}
