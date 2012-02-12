--
-- PostgreSQL database dump
--

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: pyncftp; Type: DATABASE; Schema: -; Owner: fabio
--

CREATE DATABASE pyncftp WITH TEMPLATE = template0 ENCODING = 'UTF8' LC_COLLATE = 'es_ES.UTF-8' LC_CTYPE = 'es_ES.UTF-8';


ALTER DATABASE pyncftp OWNER TO fabio;

\connect pyncftp

SET statement_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SET check_function_bodies = false;
SET client_min_messages = warning;

--
-- Name: plpgsql; Type: EXTENSION; Schema: -; Owner: 
--

CREATE EXTENSION IF NOT EXISTS plpgsql WITH SCHEMA pg_catalog;


--
-- Name: EXTENSION plpgsql; Type: COMMENT; Schema: -; Owner: 
--

COMMENT ON EXTENSION plpgsql IS 'PL/pgSQL procedural language';


SET search_path = public, pg_catalog;

SET default_tablespace = '';

SET default_with_oids = false;

--
-- Name: configuracion; Type: TABLE; Schema: public; Owner: fabio; Tablespace: 
--

CREATE TABLE configuracion (
    id integer NOT NULL,
    customer character varying,
    comment character varying,
    path character varying DEFAULT '/'::character varying,
    host character varying NOT NULL,
    type character varying DEFAULT 'ftp'::character varying NOT NULL
);


ALTER TABLE public.configuracion OWNER TO fabio;

--
-- Name: TABLE configuracion; Type: COMMENT; Schema: public; Owner: fabio
--

COMMENT ON TABLE configuracion IS 'Configuracion de clientes y ruta';


--
-- Name: configuracion_id_seq; Type: SEQUENCE; Schema: public; Owner: fabio
--

CREATE SEQUENCE configuracion_id_seq
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.configuracion_id_seq OWNER TO fabio;

--
-- Name: configuracion_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: fabio
--

ALTER SEQUENCE configuracion_id_seq OWNED BY configuracion.id;


--
-- Name: configuracion_id_seq; Type: SEQUENCE SET; Schema: public; Owner: fabio
--

SELECT pg_catalog.setval('configuracion_id_seq', 1, false);


--
-- Name: id; Type: DEFAULT; Schema: public; Owner: fabio
--

ALTER TABLE configuracion ALTER COLUMN id SET DEFAULT nextval('configuracion_id_seq'::regclass);


--
-- Data for Name: configuracion; Type: TABLE DATA; Schema: public; Owner: fabio
--

COPY configuracion (id, customer, comment, path, host, type) FROM stdin;
\.


--
-- Name: configuracion_pkey; Type: CONSTRAINT; Schema: public; Owner: fabio; Tablespace: 
--

ALTER TABLE ONLY configuracion
    ADD CONSTRAINT configuracion_pkey PRIMARY KEY (id);


--
-- Name: public; Type: ACL; Schema: -; Owner: postgres
--

REVOKE ALL ON SCHEMA public FROM PUBLIC;
REVOKE ALL ON SCHEMA public FROM postgres;
GRANT ALL ON SCHEMA public TO postgres;
GRANT ALL ON SCHEMA public TO PUBLIC;


--
-- PostgreSQL database dump complete
--

