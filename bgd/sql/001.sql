ALTER TABLE "bgdapp_content"
	ADD COLUMN "type_id" integer REFERENCES "bgdapp_contentarchetype" ("id");
