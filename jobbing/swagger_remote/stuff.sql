INSERT INTO media (
	media_status_id,
    media_data,
    media_link,
    media_title,
    media_description,
    media_size,
    media_content_upload_date,
    media_content_updated_date
) VALUES ( 
	3,
	'0', 
	'http://localhost', 
	'Empty media', 
	'Default media reference', 
	0.00, 
	'2021-12-29T00:00:00Z', 
	'2021-12-29T00:00:00Z'
);

INSERT INTO skills (
	skills_name, 
	skills_media_id, 
	skills_description, 
	skills_updated_date
) VALUES (
	'N/A', 
	1, 
	'Default skill reference', 
	'2021-12-29T00:00:00Z'
);

INSERT INTO user_model (
    user_status_id,
    user_role_id,
    user_model_first_name,
    user_model_last_name,
    user_model_surname,
    user_model_birthday,
    user_model_phone_number,
    user_model_address_id,
    user_skills_id,
    user_model_registry_date,
    user_model_updated_date,
    user_model_media_id
) VALUES (
	1, 
	3, 
	'David', 
	'Lopez Torres', 
	'Alejandro', 
	'2003-01-12', 
	'3327032686', 
	2, 
	1, 
	'2021-12-29T00:00:00Z', 
	'2021-12-29T00:00:00Z', 
	1
);

INSERT INTO user_auth (
    user_auth_password,
    user_auth_pass_date,
    user_model_id,
    user_auth_updated_date,
    user_auth_name
) VALUES (
	'pbkdf2:sha256:150000$XNhTnsBI$c3a42bf1961b53286a7cbb60b489d18a00d8f54c401d636e8765ddad97935582', 
	'2021-12-29T00:00:00Z', 
	1, 
	'2021-12-29T00:00:00Z', 
	'admin'
);

----------------------------------------------------------------------------------------
----------------------------------------------------------------------------------------

-- @author: David Lopez
-- @date: April 02, 2022

-- Table: public.profession

-- DROP TABLE IF EXISTS public.profession;

CREATE TABLE IF NOT EXISTS public.profession
(
    profession_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    profession_user integer,
    profession_skill integer,
    CONSTRAINT pk_profession PRIMARY KEY (profession_id),
    CONSTRAINT fk_user_in_profession FOREIGN KEY (profession_user)
        REFERENCES public.user_model (user_model_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_skill_in_profession FOREIGN KEY (profession_skill)
        REFERENCES public.skills (skills_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.profession
    OWNER to hpmdjukqgaxdnl;

-- Table: public.evidence

-- DROP TABLE IF EXISTS public.evidence;

CREATE TABLE IF NOT EXISTS public.evidence
(
    evidence_id integer NOT NULL GENERATED ALWAYS AS IDENTITY ( INCREMENT 1 START 1 MINVALUE 1 MAXVALUE 2147483647 CACHE 1 ),
    evidence_profession integer,
	evidence_media integer,
    CONSTRAINT pk_evidence PRIMARY KEY (evidence_id),
    CONSTRAINT fk_profession_in_evidence FOREIGN KEY (evidence_profession)
        REFERENCES public.profession (profession_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID,
    CONSTRAINT fk_media_in_evidence FOREIGN KEY (evidence_media)
        REFERENCES public.media (media_id) MATCH SIMPLE
        ON UPDATE NO ACTION
        ON DELETE NO ACTION
        NOT VALID
)

TABLESPACE pg_default;

ALTER TABLE IF EXISTS public.evidence
    OWNER to hpmdjukqgaxdnl;