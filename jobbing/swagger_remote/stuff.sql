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