'use client';

import { FormEvent, useEffect, useMemo, useState } from 'react';

type Language = 'zh' | 'en';
type JobStatus = 'queued' | 'running' | 'completed' | 'failed' | 'cancelled';

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
};

const API_BASE = '/api';
const LANGUAGE_STORAGE_KEY = 'doc-getter-language';

const COPY = {
    zh: {
        pageTitle: '在线文档抓取与 ZIP 下载',
        pageDescription: '输入文档 URL，抓取完成后直接下载 ZIP。',
        startTitle: '开始抓取',
        urlLabel: '文档 URL',
        submit: '开始抓取并打包',
        submitting: '正在提交…',
        cancel: '取消任务',
        resultTitle: '下载结果',
        resultEmpty: '提交后会自动轮询状态。完成后，这里会出现 ZIP 下载按钮。',
        inProgress: '正在抓取和打包，请稍候…',
        downloadZip: '下载 ZIP 压缩包',
        retentionHint: '这是一个临时下载结果，服务会按保留策略自动清理旧文件。',
        pages: '页面数',
        skipped: '跳过',
        createFailed: '创建任务失败',
        pollFailed: '读取任务状态失败',
        cancelFailed: '取消任务失败',
        languageLabel: '语言切换',
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
        resultEmpty: 'After submission, the page will poll automatically and show a ZIP download button when the job finishes.',
        inProgress: 'Crawling and packaging are in progress. Please wait…',
        downloadZip: 'Download ZIP archive',
        retentionHint: 'This is a temporary download result and old files are cleaned up automatically.',
        pages: 'Pages',
        skipped: 'Skipped',
        createFailed: 'Failed to create the job',
        pollFailed: 'Failed to read the job status',
        cancelFailed: 'Failed to cancel the job',
        languageLabel: 'Language switch',
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
    if (!path) {
        return '';
    }
    if (path.startsWith('http://') || path.startsWith('https://')) {
        return path;
    }
    return `${apiBase}${path}`;
}

export default function HomePage() {
    const [language, setLanguage] = useState<Language>('zh');
    const [startUrl, setStartUrl] = useState('https://openrouter.ai/docs/');
    const [job, setJob] = useState<CrawlJob | null>(null);
    const [submitting, setSubmitting] = useState(false);
    const [error, setError] = useState('');

    useEffect(() => {
        setLanguage(detectPreferredLanguage());
    }, []);

    useEffect(() => {
        if (typeof window === 'undefined') {
            return;
        }
        window.localStorage.setItem(LANGUAGE_STORAGE_KEY, language);
        document.documentElement.lang = language === 'zh' ? 'zh-CN' : 'en';
    }, [language]);

    const t = COPY[language];
    const statusLabels = STATUS_LABELS[language];

    const isFinished = useMemo(
        () => (job ? ['completed', 'failed', 'cancelled'].includes(job.status) : false),
        [job],
    );

    async function refreshJob(jobId: string) {
        const response = await fetch(`${API_BASE}/v1/crawls/${jobId}`, { cache: 'no-store' });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail ?? t.pollFailed);
        }
        setJob(data);
    }

    useEffect(() => {
        if (!job || isFinished) {
            return;
        }

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

        setSubmitting(true);
        try {
            const response = await fetch(`${API_BASE}/v1/crawls`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({
                    start_url: startUrl,
                }),
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
        if (!job) {
            return;
        }
        setError('');
        try {
            const response = await fetch(toAbsoluteUrl(API_BASE, job.cancel_url), {
                method: 'POST',
            });
            const data = await response.json();
            if (!response.ok) {
                throw new Error(data.detail ?? t.cancelFailed);
            }
            setJob(data);
        } catch (cause: unknown) {
            setError(cause instanceof Error ? cause.message : t.cancelFailed);
        }
    }

    return (
        <main className="page">
            <div className="topBar">
                <p className="eyebrow">txzy/tool/getdoc</p>

                <div className="languageSwitcher" role="group" aria-label={t.languageLabel}>
                    <button
                        type="button"
                        className={`toggleButton ${language === 'zh' ? 'active' : ''}`}
                        onClick={() => setLanguage('zh')}
                    >
                        中文
                    </button>
                    <button
                        type="button"
                        className={`toggleButton ${language === 'en' ? 'active' : ''}`}
                        onClick={() => setLanguage('en')}
                    >
                        EN
                    </button>
                </div>
            </div>

            <section className="hero card">
                <h1>{t.pageTitle}</h1>
                <p className="muted">{t.pageDescription}</p>
            </section>

            <section className="card">
                <h2>{t.startTitle}</h2>

                <form className="formGrid" onSubmit={handleSubmit}>
                    <label className="field fieldSpan">
                        <span>{t.urlLabel}</span>
                        <input
                            required
                            value={startUrl}
                            onChange={(event) => setStartUrl(event.target.value)}
                            placeholder="https://openrouter.ai/docs/"
                        />
                    </label>

                    <div className="actions fieldSpan">
                        <button type="submit" disabled={submitting}>
                            {submitting ? t.submitting : t.submit}
                        </button>
                        {job && !isFinished ? (
                            <button type="button" className="secondary" onClick={handleCancel}>
                                {t.cancel}
                            </button>
                        ) : null}
                    </div>
                </form>

                {error ? <p className="error">{error}</p> : null}
            </section>

            <section className="card">
                <h2>{t.resultTitle}</h2>
                {!job ? (
                    <p className="muted">{t.resultEmpty}</p>
                ) : (
                    <>
                        <div className="statusRow">
                            <span className={`badge badge-${job.status}`}>{statusLabels[job.status]}</span>
                            <span>
                                {t.pages}: {job.page_count}
                            </span>
                            <span>
                                {t.skipped}: {job.skipped_count}
                            </span>
                        </div>

                        {job.status === 'queued' || job.status === 'running' ? <p className="muted">{t.inProgress}</p> : null}

                        {job.status === 'completed' ? (
                            <div className="actions">
                                <a
                                    className="buttonLink"
                                    href={toAbsoluteUrl(API_BASE, job.archive_url)}
                                    target="_blank"
                                    rel="noreferrer"
                                >
                                    {t.downloadZip}
                                </a>
                            </div>
                        ) : null}

                        {job.status === 'completed' ? <p className="muted">{t.retentionHint}</p> : null}

                        {job.error ? <p className="error">{job.error}</p> : null}
                    </>
                )}
            </section>
        </main>
    );
}
