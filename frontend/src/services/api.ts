import axios from 'axios';

const API_BASE_URL = import.meta.env.VITE_API_URL || '/api';

const api = axios.create({
  baseURL: API_BASE_URL,
  headers: {
    'Content-Type': 'application/json',
  },
});

export interface Item {
  id: number;
  title: string;
  description: string | null;
  completed: boolean;
  created_at: string;
}

export interface ItemCreate {
  title: string;
  description?: string;
  completed?: boolean;
}

export interface ItemUpdate {
  title?: string;
  description?: string;
  completed?: boolean;
}

export const itemsApi = {
  list: async (): Promise<Item[]> => {
    const response = await api.get('/items');
    return response.data;
  },

  get: async (id: number): Promise<Item> => {
    const response = await api.get(`/items/${id}`);
    return response.data;
  },

  create: async (item: ItemCreate): Promise<Item> => {
    const response = await api.post('/items', item);
    return response.data;
  },

  update: async (id: number, item: ItemUpdate): Promise<Item> => {
    const response = await api.put(`/items/${id}`, item);
    return response.data;
  },

  delete: async (id: number): Promise<void> => {
    await api.delete(`/items/${id}`);
  },
};
