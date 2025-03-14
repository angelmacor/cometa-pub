export interface ApiResponse<T> {
  success: boolean;
  data?: T;
  status?: number;
  message?: string;
  error?: {
    detail?: string;
  };
}

export interface ApiError {
  success: false;
  message: string;
  status?: number;
}