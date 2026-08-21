import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const blog = defineCollection({
  loader: glob({ pattern: '**/*.{md,mdx}', base: './src/content/blog' }),
  schema: z.object({
    title: z.string(),
    description: z.string().optional().default(''),
    date: z.coerce.date().optional(),
    lastmod: z.coerce.date().optional(),
    slug: z.string().optional(),
    images: z.array(z.string()).optional().default([]),
    image: z.string().optional(),
    categories: z.array(z.string()).optional().default([]),
    tags: z.array(z.string()).optional().default([]),
    author: z.string().optional().default('PeopleNext'),
  }),
});

export const collections = {
  blog,
};
