'use client';

import { FormEvent, useEffect, useMemo, useState } from 'react';

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

function normalizeApiBase(value: string) {
    return value.replace(/\/$/, '').replace('://0.0.0.0', '://127.0.0.1');
}

const API_BASE = normalizeApiBase(process.env.NEXT_PUBLIC_API_BASE_URL ?? '');

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
    const [startUrl, setStartUrl] = useState('https://openrouter.ai/docs/');
    const [job, setJob] = useState<CrawlJob | null>(null);
    const [submitting, setSubmitting] = useState(false);
    const [error, setError] = useState('');

    const isFinished = useMemo(
        () => (job ? ['completed', 'failed', 'cancelled'].includes(job.status) : false),
        [job],
    );

    async function refreshJob(jobId: string) {
        const response = await fetch(`${API_BASE}/v1/crawls/${jobId}`, { cache: 'no-store' });
        const data = await response.json();
        if (!response.ok) {
            throw new Error(data.detail ?? '读取任务状态失败');
        }
        setJob(data);
    }

    useEffect(() => {
        if (!job || !API_BASE || isFinished) {
            return;
        }

        const timer = window.setInterval(() => {
            refreshJob(job.job_id).catch((cause: unknown) => {
                setError(cause instanceof Error ? cause.message : '轮询任务状态失败');
            });
        }, 2500);

        return () => window.clearInterval(timer);
    }, [isFinished, job]);

    async function handleSubmit(event: FormEvent<HTMLFormElement>) {
        event.preventDefault();
        setError('');
        setJob(null);

        if (!API_BASE) {
            setError('请在 web/.env.local 里设置 NEXT_PUBLIC_API_BASE_URL=http://127.0.0.1:8000。');
            return;
        }

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
                throw new Error(data.detail ?? '创建任务失败');
            }
            setJob(data);
        } catch (cause: unknown) {
            setError(cause instanceof Error ? cause.message : '创建任务失败');
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
                throw new Error(data.detail ?? '取消任务失败');
            }
            setJob(data);
        } catch (cause: unknown) {
            setError(cause instanceof Error ? cause.message : '取消任务失败');
        }
    }

    return (
        <main className="page">
            <section className="hero card">
                <p className="eyebrow">Doc Getter</p>
                <h1>在线文档抓取与 ZIP 下载</h1>
                <p className="muted">只需要填写文档 URL。服务会在独立临时目录中抓取、打包，并在完成后提供 ZIP 下载。</p>
            </section>

            <section className="card">
                <h2>开始抓取</h2>
                <p className="muted">
                    当前后端：<code>{API_BASE || '未配置'}</code>
                </p>

                <form className="formGrid" onSubmit={handleSubmit}>
                    <label className="field fieldSpan">
                        <span>文档 URL</span>
                        <input
                            required
                            value={startUrl}
                            onChange={(event) => setStartUrl(event.target.value)}
                            placeholder="https://openrouter.ai/docs/"
                        />
                    </label>

                    <div className="actions fieldSpan">
                        <button type="submit" disabled={submitting}>
                            {submitting ? '正在提交…' : '开始抓取并打包'}
                        </button>
                        {job && !isFinished ? (
                            <button type="button" className="secondary" onClick={handleCancel}>
                                取消任务
                            </button>
                        ) : null}
                    </div>
                </form>

                {!API_BASE ? (
                    <p className="error">请在前端环境变量里使用 `http://127.0.0.1:8000`，不要使用 `0.0.0.0`。</p>
                ) : null}
                {error ? <p className="error">{error}</p> : null}
            </section>

            <section className="card">
                <h2>下载结果</h2>
                {!job ? (
                    <p className="muted">提交后会自动轮询状态。完成后，这里会出现 ZIP 下载按钮。</p>
                ) : (
                    <>
                        <div className="statusRow">
                            <span className={`badge badge-${job.status}`}>{job.status}</span>
                            <span>Pages: {job.page_count}</span>
                            <span>Skipped: {job.skipped_count}</span>
                        </div>

                        {job.status === 'queued' || job.status === 'running' ? (
                            <p className="muted">正在抓取和打包，请稍候…</p>
                        ) : null}

                        {job.status === 'completed' ? (
                            <div className="links">
                                <a href={toAbsoluteUrl(API_BASE, job.archive_url)} target="_blank" rel="noreferrer">
                                    下载 ZIP 压缩包
                                </a>
                            </div>
                        ) : null}

                        {job.status === 'completed' ? (
                            <p className="muted">这是一个临时下载结果，服务会按保留策略自动清理旧文件。</p>
                        ) : null}

                        {job.error ? <p className="error">{job.error}</p> : null}
                    </>
                )}
            </section>
        </main>
    );
}
