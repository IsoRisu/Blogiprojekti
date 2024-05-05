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

CREATE TABLE public.admins(
    id serial primary key,
    user_id integer references users
);

CREATE TABLE public.groups (
    id serial primary key,
    group_name text
);

CREATE TABLE public.blog_groups (
    id serial primary key,
    group_id integer references groups on delete cascade,
    blog_id integer references blogs on delete cascade

)


CREATE TABLE public.votes (
    id serial primary key,
    blog_id integer references blogs ON DELETE CASCADE,
    user_id integer references users,
    vote integer default 0
);

CREATE TABLE public.comments (
    id serial primary key,
    blog_id integer references blogs on delete cascade,
    user_id integer references users on delete cascade,
    username text,
    content text,
    date_posted timestamp
    
);


