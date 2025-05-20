import React from "react";

async function getCategories() {
  const res = await fetch("http://localhost:8000/api/v1/categories", {
    cache: "no-store",
  });
  if (!res.ok) throw new Error("Failed to fetch categories");
  const data = await res.json();
  return data.map((cat: { name: string }) => cat.name);
}

export default async function Home() {
  let categories: string[] = [];
  let error: string | null = null;
  try {
    categories = await getCategories();
  } catch (err) {
    if (err instanceof Error) {
      error = err.message;
    } else {
      error = "Unknown error";
    }
  }

  return (
    <main className="min-h-screen flex flex-col items-center justify-center">
      <h1 className="text-3xl font-bold mb-6">Trending Categories</h1>
      {error && <p className="text-red-500">{error}</p>}
      {!error && (
        <ul className="space-y-3">
          {categories.map((cat) => (
            <li key={cat} className="px-4 py-2 bg-gray-100 dark:bg-gray-800 rounded shadow">
              {cat}
            </li>
          ))}
        </ul>
      )}
    </main>
  );
}
