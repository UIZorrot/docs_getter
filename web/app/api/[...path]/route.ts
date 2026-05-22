import { NextRequest } from 'next/server';

export const dynamic = 'force-dynamic';

function getApiBase() {
    return (process.env.DOC_GETTER_API_BASE_URL ?? process.env.NEXT_PUBLIC_API_BASE_URL ?? 'http://127.0.0.1:8000')
        .replace(/\/$/, '')
        .replace('://0.0.0.0', '://127.0.0.1');
}

async function handleProxy(
    request: NextRequest,
    context: { params: Promise<{ path?: string[] }> },
) {
    const { path = [] } = await context.params;
    const upstreamUrl = new URL(`${getApiBase()}/${path.join('/')}`);

    request.nextUrl.searchParams.forEach((value, key) => {
        upstreamUrl.searchParams.append(key, value);
    });

    const headers = new Headers(request.headers);
    headers.delete('host');
    headers.delete('origin');
    headers.delete('referer');
    headers.delete('content-length');

    const init: RequestInit = {
        method: request.method,
        headers,
        redirect: 'follow',
    };

    if (!['GET', 'HEAD'].includes(request.method)) {
        init.body = await request.arrayBuffer();
    }

    const upstreamResponse = await fetch(upstreamUrl, init);
    const responseHeaders = new Headers(upstreamResponse.headers);
    responseHeaders.delete('content-encoding');
    responseHeaders.delete('content-length');
    responseHeaders.delete('transfer-encoding');

    return new Response(upstreamResponse.body, {
        status: upstreamResponse.status,
        statusText: upstreamResponse.statusText,
        headers: responseHeaders,
    });
}

export { handleProxy as GET, handleProxy as POST, handleProxy as PUT, handleProxy as PATCH, handleProxy as DELETE, handleProxy as OPTIONS, handleProxy as HEAD };
