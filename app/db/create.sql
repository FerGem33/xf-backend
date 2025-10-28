CREATE SCHEMA IF NOT EXISTS public;

-- Categories
CREATE TABLE IF NOT EXISTS public.categories (
    category_id SERIAL PRIMARY KEY,
    category VARCHAR(50) NOT NULL,
    color VARCHAR(20),
    icon VARCHAR(50) NOT NULL
);

-- Entries
CREATE TABLE IF NOT EXISTS public.entries (
    entry_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    date DATE NOT NULL DEFAULT CURRENT_DATE,
    category_id INTEGER NOT NULL,
    CONSTRAINT fk_entry_category FOREIGN KEY (category_id)
        REFERENCES public.categories (category_id)
        ON DELETE CASCADE
);

-- Images
CREATE TABLE IF NOT EXISTS public.images (
    image_id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    entry_id INTEGER NOT NULL,
    CONSTRAINT fk_image_entry FOREIGN KEY (entry_id)
        REFERENCES public.entries (entry_id)
        ON DELETE CASCADE
);

-- Date Ideas
CREATE TABLE IF NOT EXISTS public.date_ideas (
    idea_id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT,
    category_id INTEGER,
    CONSTRAINT fk_idea_category FOREIGN KEY (category_id)
        REFERENCES public.categories (category_id)
        ON DELETE SET NULL
);

-- Links
CREATE TABLE IF NOT EXISTS public.links (
    link_id SERIAL PRIMARY KEY,
    url VARCHAR(255) NOT NULL,
    type VARCHAR(50),
    idea_id INTEGER NOT NULL,
    CONSTRAINT fk_link_idea FOREIGN KEY (idea_id)
        REFERENCES public.date_ideas (idea_id)
        ON DELETE CASCADE
);



-- Reset sequence for entries
SELECT setval('entries_entry_id_seq', (SELECT COALESCE(MAX(entry_id), 0) FROM entries));

-- Reset sequence for images
SELECT setval('images_image_id_seq', (SELECT COALESCE(MAX(image_id), 0) FROM images));

-- Reset sequence for categories
SELECT setval('categories_category_id_seq', (SELECT COALESCE(MAX(category_id), 0) FROM categories));

-- Reset sequence for date_ideas
SELECT setval('date_ideas_idea_id_seq', (SELECT COALESCE(MAX(idea_id), 0) FROM date_ideas));

-- Reset sequence for links
SELECT setval('links_link_id_seq', (SELECT COALESCE(MAX(link_id), 0) FROM links));
