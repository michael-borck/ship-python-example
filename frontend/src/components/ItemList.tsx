import { useQuery, useMutation, useQueryClient } from '@tanstack/react-query';
import { itemsApi, Item, ItemCreate } from '../services/api';
import { useState } from 'react';

export function ItemList() {
  const queryClient = useQueryClient();
  const [newTitle, setNewTitle] = useState('');

  const { data: items, isLoading, error } = useQuery({
    queryKey: ['items'],
    queryFn: itemsApi.list,
  });

  const createMutation = useMutation({
    mutationFn: (item: ItemCreate) => itemsApi.create(item),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
      setNewTitle('');
    },
  });

  const toggleMutation = useMutation({
    mutationFn: ({ id, completed }: { id: number; completed: boolean }) =>
      itemsApi.update(id, { completed }),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });

  const deleteMutation = useMutation({
    mutationFn: (id: number) => itemsApi.delete(id),
    onSuccess: () => {
      queryClient.invalidateQueries({ queryKey: ['items'] });
    },
  });

  if (isLoading) return <div>Loading...</div>;
  if (error) return <div>Error loading items</div>;

  return (
    <div className="item-list">
      <form
        onSubmit={(e) => {
          e.preventDefault();
          if (newTitle.trim()) {
            createMutation.mutate({ title: newTitle });
          }
        }}
      >
        <input
          type="text"
          value={newTitle}
          onChange={(e) => setNewTitle(e.target.value)}
          placeholder="Add new item..."
        />
        <button type="submit">Add</button>
      </form>

      <ul>
        {items?.map((item: Item) => (
          <li key={item.id}>
            <input
              type="checkbox"
              checked={item.completed}
              onChange={() =>
                toggleMutation.mutate({
                  id: item.id,
                  completed: !item.completed,
                })
              }
            />
            <span className={item.completed ? 'completed' : ''}>
              {item.title}
            </span>
            <button onClick={() => deleteMutation.mutate(item.id)}>
              Delete
            </button>
          </li>
        ))}
      </ul>
    </div>
  );
}
