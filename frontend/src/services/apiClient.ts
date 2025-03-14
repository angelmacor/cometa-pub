import { ApiResponse } from "@/types/api";

const API_TIMEOUT = 5000;

const fetchWithTimeout = async <T>(url: string, options: RequestInit = {}): Promise<ApiResponse<T>> => {
    const controller = new AbortController();
    const timeoutId = setTimeout(() => controller.abort(), API_TIMEOUT);

    try {
        const response = await fetch(url, { ...options, signal: controller.signal });
        clearTimeout(timeoutId);

        const data = await response.json().catch(() => null); 

        if (!response.ok) {
            return {
                success: false,
                status: response.status,
                message: data?.detail || `HTTP error ${response.status}`,
            };
        }

        return { success: true, data };
    } catch (error: unknown) {
        return {
            success: false,
            message: error instanceof Error
                ? error.name === "AbortError"
                    ? "Request timeout"
                    : error.message || "Network error"
                : "Unknown error occurred",
        };
    }
};

export const post = async <T>(url: string, body: unknown, headers = {}) => {
    return fetchWithTimeout<T>(url, {
        method: "POST",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            ...headers,
        },
        body: JSON.stringify(body),
    });
};

export const get = async <T>(url: string, headers = {}) => {
    return fetchWithTimeout<T>(url, {
        method: "GET",
        mode: "cors",
        headers: {
            "Content-Type": "application/json",
            ...headers,
        },
    });
};
