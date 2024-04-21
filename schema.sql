-- Users table
CREATE TABLE public.users (
    id serial primary key,
    username text unique,
    password text
);

CREATE TABLE public.blogs (
    id serial primary key,
    author text,
    title text,
    content text,
    date_posted timestamp
    
);

CREATE TABLE public.votes (
    id serial primary key,
    vote integer
);


