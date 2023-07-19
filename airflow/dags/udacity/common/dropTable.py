DROP_staging_events ="""
DROP TABLE IF EXISTS public.staging_events
"""
DROP_staging_songs = """
DROP TABLE IF EXISTS public.staging_songs
"""
DROP_artists = """

DROP TABLE IF EXISTS public.artists;
"""
DROP_songs = """
DROP TABLE IF EXISTS public.songs;
"""
DROP_users = """

DROP TABLE IF EXISTS public.users;
"""
DROP_time = """
DROP TABLE IF EXISTS public.time;
"""
DROP_songplays = """
DROP TABLE IF EXISTS public.songplays;
"""