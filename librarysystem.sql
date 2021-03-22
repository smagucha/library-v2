BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "django_migrations" (
	"id"	integer NOT NULL,
	"app"	varchar(255) NOT NULL,
	"name"	varchar(255) NOT NULL,
	"applied"	datetime NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_group_permissions" (
	"id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_groups" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"group_id"	integer NOT NULL,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("group_id") REFERENCES "auth_group"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user_user_permissions" (
	"id"	integer NOT NULL,
	"user_id"	integer NOT NULL,
	"permission_id"	integer NOT NULL,
	FOREIGN KEY("permission_id") REFERENCES "auth_permission"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_admin_log" (
	"id"	integer NOT NULL,
	"action_time"	datetime NOT NULL,
	"object_id"	text,
	"object_repr"	varchar(200) NOT NULL,
	"change_message"	text NOT NULL,
	"content_type_id"	integer,
	"user_id"	integer NOT NULL,
	"action_flag"	smallint unsigned NOT NULL CHECK("action_flag" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "django_content_type" (
	"id"	integer NOT NULL,
	"app_label"	varchar(100) NOT NULL,
	"model"	varchar(100) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_permission" (
	"id"	integer NOT NULL,
	"content_type_id"	integer NOT NULL,
	"codename"	varchar(100) NOT NULL,
	"name"	varchar(255) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("content_type_id") REFERENCES "django_content_type"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "auth_group" (
	"id"	integer NOT NULL,
	"name"	varchar(150) NOT NULL UNIQUE,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "auth_user" (
	"id"	integer NOT NULL,
	"password"	varchar(128) NOT NULL,
	"last_login"	datetime,
	"is_superuser"	bool NOT NULL,
	"username"	varchar(150) NOT NULL UNIQUE,
	"last_name"	varchar(150) NOT NULL,
	"email"	varchar(254) NOT NULL,
	"is_staff"	bool NOT NULL,
	"is_active"	bool NOT NULL,
	"date_joined"	datetime NOT NULL,
	"first_name"	varchar(150) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "django_session" (
	"session_key"	varchar(40) NOT NULL,
	"session_data"	text NOT NULL,
	"expire_date"	datetime NOT NULL,
	PRIMARY KEY("session_key")
);
CREATE TABLE IF NOT EXISTS "libraryv2_bookcatergory" (
	"id"	integer NOT NULL,
	"name"	varchar(200) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "libraryv2_bookformat" (
	"id"	integer NOT NULL,
	"Bookformat"	varchar(9) NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "libraryv2_bookissue" (
	"id"	integer NOT NULL,
	"given_date"	datetime NOT NULL,
	"book_id"	integer NOT NULL,
	"student_id"	integer NOT NULL,
	"due_date"	date NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("book_id") REFERENCES "libraryv2_book"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("student_id") REFERENCES "libraryv2_person"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "libraryv2_requestbook" (
	"id"	integer NOT NULL,
	"title"	varchar(200) NOT NULL,
	"catergory_id"	integer NOT NULL,
	"yourname_id"	integer NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("yourname_id") REFERENCES "libraryv2_person"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("catergory_id") REFERENCES "libraryv2_bookcatergory"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "libraryv2_librarian" (
	"id"	integer NOT NULL,
	"phone"	integer unsigned NOT NULL CHECK("phone" >= 0),
	"librarianid"	varchar(200) NOT NULL,
	"user_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "libraryv2_person" (
	"id"	integer NOT NULL,
	"phone"	integer unsigned NOT NULL CHECK("phone" >= 0),
	"studentid"	varchar(200) NOT NULL,
	"user_id"	integer,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("user_id") REFERENCES "auth_user"("id") DEFERRABLE INITIALLY DEFERRED
);
CREATE TABLE IF NOT EXISTS "libraryv2_book" (
	"id"	integer NOT NULL,
	"title"	varchar(200) NOT NULL,
	"subject"	varchar(200) NOT NULL,
	"publisher"	varchar(200) NOT NULL,
	"authors"	varchar(200) NOT NULL,
	"catergory_id"	integer NOT NULL,
	"formatt_id"	integer NOT NULL,
	"availablebook"	integer unsigned NOT NULL CHECK("availablebook" >= 0),
	"givenout"	integer unsigned CHECK("givenout" >= 0),
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("formatt_id") REFERENCES "libraryv2_bookformat"("id") DEFERRABLE INITIALLY DEFERRED,
	FOREIGN KEY("catergory_id") REFERENCES "libraryv2_bookcatergory"("id") DEFERRABLE INITIALLY DEFERRED
);
INSERT INTO "django_migrations" VALUES (1,'contenttypes','0001_initial','2021-02-13 08:13:39.754602');
INSERT INTO "django_migrations" VALUES (2,'auth','0001_initial','2021-02-13 08:13:40.014692');
INSERT INTO "django_migrations" VALUES (3,'admin','0001_initial','2021-02-13 08:13:40.369531');
INSERT INTO "django_migrations" VALUES (4,'admin','0002_logentry_remove_auto_add','2021-02-13 08:13:40.794479');
INSERT INTO "django_migrations" VALUES (5,'admin','0003_logentry_add_action_flag_choices','2021-02-13 08:13:41.159337');
INSERT INTO "django_migrations" VALUES (6,'contenttypes','0002_remove_content_type_name','2021-02-13 08:13:41.529493');
INSERT INTO "django_migrations" VALUES (7,'auth','0002_alter_permission_name_max_length','2021-02-13 08:13:41.894641');
INSERT INTO "django_migrations" VALUES (8,'auth','0003_alter_user_email_max_length','2021-02-13 08:13:42.219822');
INSERT INTO "django_migrations" VALUES (9,'auth','0004_alter_user_username_opts','2021-02-13 08:13:42.514797');
INSERT INTO "django_migrations" VALUES (10,'auth','0005_alter_user_last_login_null','2021-02-13 08:13:42.819860');
INSERT INTO "django_migrations" VALUES (11,'auth','0006_require_contenttypes_0002','2021-02-13 08:13:43.014908');
INSERT INTO "django_migrations" VALUES (12,'auth','0007_alter_validators_add_error_messages','2021-02-13 08:13:43.639815');
INSERT INTO "django_migrations" VALUES (13,'auth','0008_alter_user_username_max_length','2021-02-13 08:13:43.944389');
INSERT INTO "django_migrations" VALUES (14,'auth','0009_alter_user_last_name_max_length','2021-02-13 08:13:44.239759');
INSERT INTO "django_migrations" VALUES (15,'auth','0010_alter_group_name_max_length','2021-02-13 08:13:44.534389');
INSERT INTO "django_migrations" VALUES (16,'auth','0011_update_proxy_permissions','2021-02-13 08:13:44.924837');
INSERT INTO "django_migrations" VALUES (17,'auth','0012_alter_user_first_name_max_length','2021-02-13 08:13:45.357226');
INSERT INTO "django_migrations" VALUES (18,'sessions','0001_initial','2021-02-13 08:13:45.579632');
INSERT INTO "django_migrations" VALUES (19,'libraryv2','0001_initial','2021-02-13 08:21:35.672171');
INSERT INTO "django_migrations" VALUES (20,'libraryv2','0002_auto_20210213_1138','2021-02-13 08:38:08.717355');
INSERT INTO "django_migrations" VALUES (21,'libraryv2','0003_requestbook','2021-02-17 12:11:36.217040');
INSERT INTO "django_migrations" VALUES (22,'libraryv2','0004_auto_20210219_1531','2021-02-19 12:31:13.439689');
INSERT INTO "django_migrations" VALUES (23,'libraryv2','0005_auto_20210219_1546','2021-02-19 12:46:55.459905');
INSERT INTO "django_migrations" VALUES (24,'libraryv2','0006_delete_requestbook','2021-02-22 07:53:44.033999');
INSERT INTO "django_migrations" VALUES (25,'libraryv2','0007_requestbook','2021-02-22 07:53:44.242222');
INSERT INTO "django_migrations" VALUES (26,'libraryv2','0008_auto_20210222_1106','2021-02-22 08:07:03.619099');
INSERT INTO "django_migrations" VALUES (27,'libraryv2','0009_auto_20210222_1204','2021-02-22 09:04:38.527839');
INSERT INTO "django_migrations" VALUES (28,'libraryv2','0010_auto_20210302_0806','2021-03-02 05:06:17.630220');
INSERT INTO "django_migrations" VALUES (29,'libraryv2','0011_auto_20210305_1219','2021-03-05 09:19:39.673085');
INSERT INTO "django_migrations" VALUES (30,'libraryv2','0012_book_givenout','2021-03-05 09:22:16.139542');
INSERT INTO "auth_group_permissions" VALUES (1,1,33);
INSERT INTO "auth_group_permissions" VALUES (2,1,34);
INSERT INTO "auth_group_permissions" VALUES (3,1,35);
INSERT INTO "auth_group_permissions" VALUES (4,1,36);
INSERT INTO "auth_group_permissions" VALUES (5,1,37);
INSERT INTO "auth_group_permissions" VALUES (6,1,38);
INSERT INTO "auth_group_permissions" VALUES (7,1,39);
INSERT INTO "auth_group_permissions" VALUES (8,1,40);
INSERT INTO "auth_group_permissions" VALUES (9,1,41);
INSERT INTO "auth_group_permissions" VALUES (10,1,42);
INSERT INTO "auth_group_permissions" VALUES (11,1,43);
INSERT INTO "auth_group_permissions" VALUES (12,1,44);
INSERT INTO "auth_group_permissions" VALUES (13,1,45);
INSERT INTO "auth_group_permissions" VALUES (14,1,46);
INSERT INTO "auth_group_permissions" VALUES (15,1,47);
INSERT INTO "auth_group_permissions" VALUES (16,1,48);
INSERT INTO "auth_group_permissions" VALUES (17,1,30);
INSERT INTO "auth_group_permissions" VALUES (18,2,1);
INSERT INTO "auth_group_permissions" VALUES (19,2,2);
INSERT INTO "auth_group_permissions" VALUES (20,2,3);
INSERT INTO "auth_group_permissions" VALUES (21,2,4);
INSERT INTO "auth_group_permissions" VALUES (22,2,5);
INSERT INTO "auth_group_permissions" VALUES (23,2,6);
INSERT INTO "auth_group_permissions" VALUES (24,2,7);
INSERT INTO "auth_group_permissions" VALUES (25,2,8);
INSERT INTO "auth_group_permissions" VALUES (26,2,9);
INSERT INTO "auth_group_permissions" VALUES (27,2,10);
INSERT INTO "auth_group_permissions" VALUES (28,2,11);
INSERT INTO "auth_group_permissions" VALUES (29,2,12);
INSERT INTO "auth_group_permissions" VALUES (30,2,13);
INSERT INTO "auth_group_permissions" VALUES (31,2,14);
INSERT INTO "auth_group_permissions" VALUES (32,2,15);
INSERT INTO "auth_group_permissions" VALUES (33,2,16);
INSERT INTO "auth_group_permissions" VALUES (34,2,17);
INSERT INTO "auth_group_permissions" VALUES (35,2,18);
INSERT INTO "auth_group_permissions" VALUES (36,2,19);
INSERT INTO "auth_group_permissions" VALUES (37,2,20);
INSERT INTO "auth_group_permissions" VALUES (38,2,21);
INSERT INTO "auth_group_permissions" VALUES (39,2,22);
INSERT INTO "auth_group_permissions" VALUES (40,2,23);
INSERT INTO "auth_group_permissions" VALUES (41,2,24);
INSERT INTO "auth_group_permissions" VALUES (42,2,25);
INSERT INTO "auth_group_permissions" VALUES (43,2,26);
INSERT INTO "auth_group_permissions" VALUES (44,2,27);
INSERT INTO "auth_group_permissions" VALUES (45,2,28);
INSERT INTO "auth_group_permissions" VALUES (46,2,29);
INSERT INTO "auth_group_permissions" VALUES (47,2,30);
INSERT INTO "auth_group_permissions" VALUES (48,2,31);
INSERT INTO "auth_group_permissions" VALUES (49,2,32);
INSERT INTO "auth_group_permissions" VALUES (50,2,33);
INSERT INTO "auth_group_permissions" VALUES (51,2,34);
INSERT INTO "auth_group_permissions" VALUES (52,2,35);
INSERT INTO "auth_group_permissions" VALUES (53,2,36);
INSERT INTO "auth_group_permissions" VALUES (54,2,37);
INSERT INTO "auth_group_permissions" VALUES (55,2,38);
INSERT INTO "auth_group_permissions" VALUES (56,2,39);
INSERT INTO "auth_group_permissions" VALUES (57,2,40);
INSERT INTO "auth_group_permissions" VALUES (58,2,41);
INSERT INTO "auth_group_permissions" VALUES (59,2,42);
INSERT INTO "auth_group_permissions" VALUES (60,2,43);
INSERT INTO "auth_group_permissions" VALUES (61,2,44);
INSERT INTO "auth_group_permissions" VALUES (62,2,45);
INSERT INTO "auth_group_permissions" VALUES (63,2,46);
INSERT INTO "auth_group_permissions" VALUES (64,2,47);
INSERT INTO "auth_group_permissions" VALUES (65,2,48);
INSERT INTO "auth_group_permissions" VALUES (66,2,49);
INSERT INTO "auth_group_permissions" VALUES (67,2,50);
INSERT INTO "auth_group_permissions" VALUES (68,2,51);
INSERT INTO "auth_group_permissions" VALUES (69,2,52);
INSERT INTO "auth_group_permissions" VALUES (70,3,49);
INSERT INTO "auth_group_permissions" VALUES (71,3,50);
INSERT INTO "auth_group_permissions" VALUES (72,3,51);
INSERT INTO "auth_group_permissions" VALUES (73,3,52);
INSERT INTO "auth_group_permissions" VALUES (74,3,26);
INSERT INTO "auth_group_permissions" VALUES (75,3,28);
INSERT INTO "auth_user_groups" VALUES (1,2,3);
INSERT INTO "auth_user_groups" VALUES (2,1,2);
INSERT INTO "auth_user_groups" VALUES (3,3,1);
INSERT INTO "auth_user_groups" VALUES (4,3,2);
INSERT INTO "auth_user_groups" VALUES (5,4,1);
INSERT INTO "auth_user_groups" VALUES (6,5,3);
INSERT INTO "auth_user_user_permissions" VALUES (1,2,41);
INSERT INTO "auth_user_user_permissions" VALUES (2,2,42);
INSERT INTO "auth_user_user_permissions" VALUES (3,2,43);
INSERT INTO "auth_user_user_permissions" VALUES (4,2,44);
INSERT INTO "django_admin_log" VALUES (1,'2021-02-13 08:41:33.529017','1','BookFormat object (1)','[{"added": {}}]',9,1,1);
INSERT INTO "django_admin_log" VALUES (2,'2021-02-13 08:41:41.060113','2','BookFormat object (2)','[{"added": {}}]',9,1,1);
INSERT INTO "django_admin_log" VALUES (3,'2021-02-13 08:41:52.042449','3','BookFormat object (3)','[{"added": {}}]',9,1,1);
INSERT INTO "django_admin_log" VALUES (4,'2021-02-13 08:41:58.523879','4','BookFormat object (4)','[{"added": {}}]',9,1,1);
INSERT INTO "django_admin_log" VALUES (5,'2021-02-13 08:42:05.436162','5','BookFormat object (5)','[{"added": {}}]',9,1,1);
INSERT INTO "django_admin_log" VALUES (6,'2021-02-17 12:34:13.675031','7','Bookissue object (7)','',12,1,3);
INSERT INTO "django_admin_log" VALUES (7,'2021-02-18 19:18:02.031265','1','Grouplibrarian','[{"added": {}}]',3,1,1);
INSERT INTO "django_admin_log" VALUES (8,'2021-02-18 19:18:58.578554','2','Groupadmin','[{"added": {}}]',3,1,1);
INSERT INTO "django_admin_log" VALUES (9,'2021-02-18 19:20:55.866508','3','studentgroup','[{"added": {}}]',3,1,1);
INSERT INTO "django_admin_log" VALUES (10,'2021-02-19 12:43:04.325776','2','cynthia mongina','',7,1,3);
INSERT INTO "django_admin_log" VALUES (11,'2021-02-19 12:43:04.604432','1','sammy otachi','',7,1,3);
INSERT INTO "django_admin_log" VALUES (12,'2021-02-19 12:43:16.355876','4','Librarian object (4)','',8,1,3);
INSERT INTO "django_admin_log" VALUES (13,'2021-02-19 12:49:43.706227','2','cynthia','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (14,'2021-02-19 12:50:02.058752','2','cynthia','[{"changed": {"fields": ["Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (15,'2021-02-19 13:33:49.359791','2','cynthia','[]',4,1,2);
INSERT INTO "django_admin_log" VALUES (16,'2021-02-19 13:48:33.666508','2','cynthia','[{"changed": {"fields": ["User permissions"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (17,'2021-02-21 06:00:27.209290','1','sam','[{"changed": {"fields": ["Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (18,'2021-02-21 06:48:41.202864','2','Groupadmin','[]',3,1,2);
INSERT INTO "django_admin_log" VALUES (19,'2021-02-21 07:02:33.368491','3','nick','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (20,'2021-02-21 07:03:21.905514','3','nick','[{"changed": {"fields": ["First name", "Last name", "Email address", "Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (21,'2021-02-21 09:22:58.852881','1','Person object (1)','[{"added": {}}]',7,1,1);
INSERT INTO "django_admin_log" VALUES (22,'2021-02-21 09:35:07.140216','4','librarian','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (23,'2021-02-21 09:35:45.417415','4','librarian','[{"changed": {"fields": ["First name", "Last name", "Email address", "Staff status", "Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (24,'2021-03-02 02:10:31.930604','5','oscar','[{"added": {}}]',4,1,1);
INSERT INTO "django_admin_log" VALUES (25,'2021-03-02 02:11:55.672320','5','oscar','[{"changed": {"fields": ["First name", "Groups"]}}]',4,1,2);
INSERT INTO "django_admin_log" VALUES (26,'2021-03-02 02:12:46.053046','2','Person object (2)','[{"added": {}}]',7,1,1);
INSERT INTO "django_admin_log" VALUES (27,'2021-03-02 05:04:37.044343','1','Librarian object (1)','[{"added": {}}]',8,1,1);
INSERT INTO "django_admin_log" VALUES (28,'2021-03-04 07:58:48.086308','2','RequestBook object (2)','[{"added": {}}]',13,1,1);
INSERT INTO "django_admin_log" VALUES (29,'2021-03-05 09:16:30.298914','2','oscar','',7,1,3);
INSERT INTO "django_admin_log" VALUES (30,'2021-03-05 09:16:30.701445','1','cynthia','',7,1,3);
INSERT INTO "django_admin_log" VALUES (31,'2021-03-05 09:20:07.473077','6','network administer','',11,1,3);
INSERT INTO "django_admin_log" VALUES (32,'2021-03-05 09:20:07.625072','5','justnow','',11,1,3);
INSERT INTO "django_admin_log" VALUES (33,'2021-03-05 09:20:07.715006','3','python pro','',11,1,3);
INSERT INTO "django_admin_log" VALUES (34,'2021-03-05 09:20:07.843576','2','css fundmental','',11,1,3);
INSERT INTO "django_admin_log" VALUES (35,'2021-03-05 09:20:52.108079','2','Librarian object (2)','',8,1,3);
INSERT INTO "django_admin_log" VALUES (36,'2021-03-05 09:20:52.284701','1','Librarian object (1)','',8,1,3);
INSERT INTO "django_admin_log" VALUES (37,'2021-03-05 09:21:22.961241','4','geography','',10,1,3);
INSERT INTO "django_admin_log" VALUES (38,'2021-03-05 09:21:23.133712','3','history','',10,1,3);
INSERT INTO "django_admin_log" VALUES (39,'2021-03-05 09:21:23.291236','2','kjkjg','',10,1,3);
INSERT INTO "django_admin_log" VALUES (40,'2021-03-05 09:21:23.388436','1','programming','',10,1,3);
INSERT INTO "django_admin_log" VALUES (41,'2021-03-05 09:35:38.993814','3','Person object (3)','[{"added": {}}]',7,1,1);
INSERT INTO "django_admin_log" VALUES (42,'2021-03-05 11:50:03.754603','6','dbjk','[{"added": {}}]',11,1,1);
INSERT INTO "django_admin_log" VALUES (43,'2021-03-18 21:40:18.007663','4','Person object (4)','[{"added": {}}]',7,1,1);
INSERT INTO "django_content_type" VALUES (1,'admin','logentry');
INSERT INTO "django_content_type" VALUES (2,'auth','permission');
INSERT INTO "django_content_type" VALUES (3,'auth','group');
INSERT INTO "django_content_type" VALUES (4,'auth','user');
INSERT INTO "django_content_type" VALUES (5,'contenttypes','contenttype');
INSERT INTO "django_content_type" VALUES (6,'sessions','session');
INSERT INTO "django_content_type" VALUES (7,'libraryv2','person');
INSERT INTO "django_content_type" VALUES (8,'libraryv2','librarian');
INSERT INTO "django_content_type" VALUES (9,'libraryv2','bookformat');
INSERT INTO "django_content_type" VALUES (10,'libraryv2','bookcatergory');
INSERT INTO "django_content_type" VALUES (11,'libraryv2','book');
INSERT INTO "django_content_type" VALUES (12,'libraryv2','bookissue');
INSERT INTO "django_content_type" VALUES (13,'libraryv2','requestbook');
INSERT INTO "auth_permission" VALUES (1,1,'add_logentry','Can add log entry');
INSERT INTO "auth_permission" VALUES (2,1,'change_logentry','Can change log entry');
INSERT INTO "auth_permission" VALUES (3,1,'delete_logentry','Can delete log entry');
INSERT INTO "auth_permission" VALUES (4,1,'view_logentry','Can view log entry');
INSERT INTO "auth_permission" VALUES (5,2,'add_permission','Can add permission');
INSERT INTO "auth_permission" VALUES (6,2,'change_permission','Can change permission');
INSERT INTO "auth_permission" VALUES (7,2,'delete_permission','Can delete permission');
INSERT INTO "auth_permission" VALUES (8,2,'view_permission','Can view permission');
INSERT INTO "auth_permission" VALUES (9,3,'add_group','Can add group');
INSERT INTO "auth_permission" VALUES (10,3,'change_group','Can change group');
INSERT INTO "auth_permission" VALUES (11,3,'delete_group','Can delete group');
INSERT INTO "auth_permission" VALUES (12,3,'view_group','Can view group');
INSERT INTO "auth_permission" VALUES (13,4,'add_user','Can add user');
INSERT INTO "auth_permission" VALUES (14,4,'change_user','Can change user');
INSERT INTO "auth_permission" VALUES (15,4,'delete_user','Can delete user');
INSERT INTO "auth_permission" VALUES (16,4,'view_user','Can view user');
INSERT INTO "auth_permission" VALUES (17,5,'add_contenttype','Can add content type');
INSERT INTO "auth_permission" VALUES (18,5,'change_contenttype','Can change content type');
INSERT INTO "auth_permission" VALUES (19,5,'delete_contenttype','Can delete content type');
INSERT INTO "auth_permission" VALUES (20,5,'view_contenttype','Can view content type');
INSERT INTO "auth_permission" VALUES (21,6,'add_session','Can add session');
INSERT INTO "auth_permission" VALUES (22,6,'change_session','Can change session');
INSERT INTO "auth_permission" VALUES (23,6,'delete_session','Can delete session');
INSERT INTO "auth_permission" VALUES (24,6,'view_session','Can view session');
INSERT INTO "auth_permission" VALUES (25,7,'add_person','Can add person');
INSERT INTO "auth_permission" VALUES (26,7,'change_person','Can change person');
INSERT INTO "auth_permission" VALUES (27,7,'delete_person','Can delete person');
INSERT INTO "auth_permission" VALUES (28,7,'view_person','Can view person');
INSERT INTO "auth_permission" VALUES (29,8,'add_librarian','Can add librarian');
INSERT INTO "auth_permission" VALUES (30,8,'change_librarian','Can change librarian');
INSERT INTO "auth_permission" VALUES (31,8,'delete_librarian','Can delete librarian');
INSERT INTO "auth_permission" VALUES (32,8,'view_librarian','Can view librarian');
INSERT INTO "auth_permission" VALUES (33,9,'add_bookformat','Can add book format');
INSERT INTO "auth_permission" VALUES (34,9,'change_bookformat','Can change book format');
INSERT INTO "auth_permission" VALUES (35,9,'delete_bookformat','Can delete book format');
INSERT INTO "auth_permission" VALUES (36,9,'view_bookformat','Can view book format');
INSERT INTO "auth_permission" VALUES (37,10,'add_bookcatergory','Can add book catergory');
INSERT INTO "auth_permission" VALUES (38,10,'change_bookcatergory','Can change book catergory');
INSERT INTO "auth_permission" VALUES (39,10,'delete_bookcatergory','Can delete book catergory');
INSERT INTO "auth_permission" VALUES (40,10,'view_bookcatergory','Can view book catergory');
INSERT INTO "auth_permission" VALUES (41,11,'add_book','Can add book');
INSERT INTO "auth_permission" VALUES (42,11,'change_book','Can change book');
INSERT INTO "auth_permission" VALUES (43,11,'delete_book','Can delete book');
INSERT INTO "auth_permission" VALUES (44,11,'view_book','Can view book');
INSERT INTO "auth_permission" VALUES (45,12,'add_bookissue','Can add bookissue');
INSERT INTO "auth_permission" VALUES (46,12,'change_bookissue','Can change bookissue');
INSERT INTO "auth_permission" VALUES (47,12,'delete_bookissue','Can delete bookissue');
INSERT INTO "auth_permission" VALUES (48,12,'view_bookissue','Can view bookissue');
INSERT INTO "auth_permission" VALUES (49,13,'add_requestbook','Can add request book');
INSERT INTO "auth_permission" VALUES (50,13,'change_requestbook','Can change request book');
INSERT INTO "auth_permission" VALUES (51,13,'delete_requestbook','Can delete request book');
INSERT INTO "auth_permission" VALUES (52,13,'view_requestbook','Can view request book');
INSERT INTO "auth_group" VALUES (1,'Grouplibrarian');
INSERT INTO "auth_group" VALUES (2,'Groupadmin');
INSERT INTO "auth_group" VALUES (3,'studentgroup');
INSERT INTO "auth_user" VALUES (1,'pbkdf2_sha256$216000$z6r6kr06F76e$gFcfMFRS32QbExXXcG2HWhfEFy3vrbs4M43B+auzHTs=','2021-03-22 13:54:00.745735',1,'sam','','',1,1,'2021-02-13 08:14:20','');
INSERT INTO "auth_user" VALUES (2,'pbkdf2_sha256$216000$GxX46iFJahjP$yUEjKv5zsPa4+7K04l/cgOtEG76scZmOUwodSoZD78E=','2021-03-04 07:00:37.141432',0,'cynthia','','',0,1,'2021-02-19 12:49:42','');
INSERT INTO "auth_user" VALUES (3,'pbkdf2_sha256$216000$7ydk6gjAd7i8$j3Uv16X12V38T7Zfju4QdmHIcauIjK1wRMifj2EK+pE=','2021-02-21 07:03:48.509255',0,'nick','nyandoro','nick@gmail.com',0,1,'2021-02-21 07:02:32','nick');
INSERT INTO "auth_user" VALUES (4,'pbkdf2_sha256$216000$SzaFxjPz6tQk$HR4sZyHtsHLyqwoxJ6BtI60MFSVwZWiLmG4DnMIkQIo=','2021-03-02 08:31:27.121293',0,'librarian','lib','lib@gmail.com',1,1,'2021-02-21 09:35:06','librarian');
INSERT INTO "auth_user" VALUES (5,'pbkdf2_sha256$216000$9JmHWu31EiG8$fBHPvqhu+NCXIcZ0e4sLGE4S44Koad+yoyIvQtW8WYM=','2021-03-18 21:40:41.237152',0,'oscar','','',0,1,'2021-03-02 02:10:31','oscar');
INSERT INTO "django_session" VALUES ('16ba0w0np9dwm3dfafjp5izsgfefp37y','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lAq6L:YNZcYqi7Q8ADtdlasegx8abJ4qYzB3TR2bultEaEgK4','2021-02-27 08:16:25.419005');
INSERT INTO "django_session" VALUES ('ctk1vieong62yyb5jq8g3a85ety7qd3f','e30:1lCek6:poQypGjAT1EOv8XniWqN-Yfxz4eXBCnTB6MbBFfg6ho','2021-03-04 08:32:58.038803');
INSERT INTO "django_session" VALUES ('6ntxz931jhlf16wjlwr720y64lzkyw81','e30:1lCeoh:fF6DKpEltbeJDklhb6_gY7makjqJ3u0nmj1vcdRcKng','2021-03-04 08:37:43.404522');
INSERT INTO "django_session" VALUES ('q36hrjakajyrrk7zdupfzjsl87ay09ia','e30:1lCfpm:if1a8o38bVJEV58q9w2tWlGjS0K1tUK28RstuRm5MzI','2021-03-04 09:42:54.815431');
INSERT INTO "django_session" VALUES ('lm1v3ltj9nmdnhimxcwuwgzptcbr3z1v','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lD23Q:uEmtbFLFzFvJ6Weu_tvhG_hvr0U2fVClJTjLlAqSbC4','2021-03-05 09:26:28.706028');
INSERT INTO "django_session" VALUES ('cigwygbov37m6lsmtb7cf9sn8h3dr52v','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lD3CA:1Rr3sf0O2FBhM0NGnowKykt6Mj4NUJh3LzNj4AI1_Wo','2021-03-05 10:39:34.714144');
INSERT INTO "django_session" VALUES ('w40el3gjbq70fopgelhy4qn6dfpxwrui','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lDZd4:9dws6EZWA2Iu634mG0RQhRmxKgFyLWa6seENU8HhvSQ','2021-03-06 21:17:30.733611');
INSERT INTO "django_session" VALUES ('uxoui0w6pr10zgleo6lp7vk7okyfn076','.eJxVjMsOgjAUBf-la9OUguXWpXu_obkvLGpKQmFl_HchYaHbMzPnbRKuS05r1TmNYi6mM6ffjZCfWnYgDyz3yfJUlnkkuyv2oNXeJtHX9XD_DjLWvNUkpLFnbqPwIADQeMfBNRo9RBgcU2iVlD11gSEobi6HnqLymcWh-XwBE-A5Yw:1lE543:3px10j9e5tt3gCDMhmBuoZamEKgvNtuHNg-n8kW-qGs','2021-03-08 06:51:27.738755');
INSERT INTO "django_session" VALUES ('f32z2o8nkmccch76jrgzyqhbmjmja2s0','.eJxVjEEOwiAQRe_C2hAyDKV16d4zkGEGpGogKe3KeHdt0oVu_3vvv1SgbS1h62kJs6izAnX63SLxI9UdyJ3qrWludV3mqHdFH7Tra5P0vBzu30GhXr41TeAj44RksiTjBSAyJR4YkhVrMzoHxowYwaIBP0ZLwJwRHQxesnp_APHzN-k:1lEA62:8TVnayqX9TFQzwcJuLzC8X8PbJFNIrMy4tIjiCdS4t8','2021-03-08 12:13:50.988748');
INSERT INTO "django_session" VALUES ('285oojnvu8cdlbz3ieq5nmax8x52l3tb','.eJxVjMsOgjAUBf-la9OUguXWpXu_obkvLGpKQmFl_HchYaHbMzPnbRKuS05r1TmNYi6mM6ffjZCfWnYgDyz3yfJUlnkkuyv2oNXeJtHX9XD_DjLWvNUkpLFnbqPwIADQeMfBNRo9RBgcU2iVlD11gSEobi6HnqLymcWh-XwBE-A5Yw:1lFiCH:SbB_1Zj4lFvaRK5nqm3byA3AP8gDNmJ4wRoxMfhm8tU','2021-03-12 18:50:41.737014');
INSERT INTO "django_session" VALUES ('do2j5nl2jw8hcpkrm362gdvgije1q9mh','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lGlJZ:toGI5E78rv__h0COGu9SijHxMDcE4R7EOfqD4_T5c18','2021-03-15 16:22:33.893200');
INSERT INTO "django_session" VALUES ('sw91c5iax170vngydfd3fnnhk35r07uk','.eJxVjM0OwiAQhN-FsyFFfnbx6N1nILAsUjU0Ke3J-O62SQ96nPm-mbcIcV1qWDvPYcziIqw4_XYp0pPbDvIjtvskaWrLPCa5K_KgXd6mzK_r4f4d1NjrtkbtjdKuABvFPnkiZxiKc2j1UNAiI4BHUBYRzmS2PIDOqpCK2qkkPl-7ZDbA:1lGy1t:l8-GeufDcR6UTGK8bl84YA-XQIXlvHyumsFTO2viVkQ','2021-03-16 05:57:09.972500');
INSERT INTO "django_session" VALUES ('lafxvv5qpifkxbsf59bq8kml3vtje0ep','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lI8fQ:JMoRSawgjAuqjzPMmoo8kiadEA889-GCl6zUZMGfURU','2021-03-19 11:30:48.057514');
INSERT INTO "django_session" VALUES ('vhcznbmmsyh74i2k13v8erc2c2wxj50k','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lIm1k:38pLYuLdTit5ZSFPb9Wloy90Tvy4VISsnW2Pv5xgPb4','2021-03-21 05:32:28.989344');
INSERT INTO "django_session" VALUES ('2gjuhxjr78pmhr89ngufxe5byz5jag3l','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lL9CI:AtviyEi3i24Z6MkpVqsSWPHNeMgQnZaGFoIa4sOT82c','2021-03-27 18:41:10.344061');
INSERT INTO "django_session" VALUES ('o5fv8hzddpu6huyelk7ih9xuzarnf639','.eJxVjM0OwiAQhN-FsyFFfnbx6N1nILAsUjU0Ke3J-O62SQ96nPm-mbcIcV1qWDvPYcziIqw4_XYp0pPbDvIjtvskaWrLPCa5K_KgXd6mzK_r4f4d1NjrtkbtjdKuABvFPnkiZxiKc2j1UNAiI4BHUBYRzmS2PIDOqpCK2qkkPl-7ZDbA:1lN0Nl:L_qanodSFkMQAS-H9aOV5iTFwcBeSw4vGlkItEmvGKk','2021-04-01 21:40:41.372587');
INSERT INTO "django_session" VALUES ('jatkxwtzkoy93bdi4ec2murlt385zzaq','.eJxVjDsOwjAQBe_iGlnxd21K-pzBWnvXOIASKZ8KcXdkKQW0b2beWyQ89paOjdc0kbgKJS6_W8by5LkDeuB8X2RZ5n2dsuyKPOkmx4X4dTvdv4OGW-t1IG-Ms8i2eNCOsvcKoHgXIsNgtaqhoo6mkolMnFEzWKwFQemhgPh8AdtROBE:1lOL0K:HbdSok_XyuNi34Ym5Aiewh8Umg3w0WOUPMtSO7WG26Q','2021-04-05 13:54:00.849732');
INSERT INTO "libraryv2_bookcatergory" VALUES (5,'science');
INSERT INTO "libraryv2_bookformat" VALUES (1,'HARDCOVER');
INSERT INTO "libraryv2_bookformat" VALUES (2,'PAPERBACK');
INSERT INTO "libraryv2_bookformat" VALUES (3,'NEWSPAPER');
INSERT INTO "libraryv2_bookformat" VALUES (4,'MAGAZINE');
INSERT INTO "libraryv2_bookformat" VALUES (5,'JOURNAL');
INSERT INTO "libraryv2_bookissue" VALUES (11,'2021-03-05 10:17:51.502483',1,3,'2021-03-18');
INSERT INTO "libraryv2_librarian" VALUES (7,55,'12548',4);
INSERT INTO "libraryv2_librarian" VALUES (8,45,'kfdkng',1);
INSERT INTO "libraryv2_person" VALUES (3,5454,'fdgnknfdl',5);
INSERT INTO "libraryv2_person" VALUES (4,1,'blbdk.c',2);
INSERT INTO "libraryv2_book" VALUES (1,'rambo last blood','science','magucha','oscar',5,1,100,NULL);
INSERT INTO "libraryv2_book" VALUES (2,'goodiies','jbskfd','bdskfjdn','bdvskdnv',5,1,4,NULL);
INSERT INTO "libraryv2_book" VALUES (3,'jdlfb','ldjknvc','vbdsk','vdsbfdn',5,1,2,NULL);
INSERT INTO "libraryv2_book" VALUES (4,'dsfnbkj','fdjkfn','wifldjsk','edkfjdn',5,1,4,NULL);
INSERT INTO "libraryv2_book" VALUES (5,'dfdkj','klfjdn7','klfjdn,',';f''ld;kln',5,1,5152,NULL);
INSERT INTO "libraryv2_book" VALUES (6,'dbjk','jbdsk','jbksfd','dsb',5,3,4,5);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_group_permissions_group_id_permission_id_0cd325b0_uniq" ON "auth_group_permissions" (
	"group_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_group_id_b120cbf9" ON "auth_group_permissions" (
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_group_permissions_permission_id_84c5c92e" ON "auth_group_permissions" (
	"permission_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_groups_user_id_group_id_94350c0c_uniq" ON "auth_user_groups" (
	"user_id",
	"group_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_user_id_6a12ed8b" ON "auth_user_groups" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_groups_group_id_97559544" ON "auth_user_groups" (
	"group_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_permission_id_14a6b632_uniq" ON "auth_user_user_permissions" (
	"user_id",
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_user_id_a95ead1b" ON "auth_user_user_permissions" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "auth_user_user_permissions_permission_id_1fbb5f2c" ON "auth_user_user_permissions" (
	"permission_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_content_type_id_c4bce8eb" ON "django_admin_log" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_admin_log_user_id_c564eba6" ON "django_admin_log" (
	"user_id"
);
CREATE UNIQUE INDEX IF NOT EXISTS "django_content_type_app_label_model_76bd3d3b_uniq" ON "django_content_type" (
	"app_label",
	"model"
);
CREATE UNIQUE INDEX IF NOT EXISTS "auth_permission_content_type_id_codename_01ab375a_uniq" ON "auth_permission" (
	"content_type_id",
	"codename"
);
CREATE INDEX IF NOT EXISTS "auth_permission_content_type_id_2f476e4b" ON "auth_permission" (
	"content_type_id"
);
CREATE INDEX IF NOT EXISTS "django_session_expire_date_a5c62663" ON "django_session" (
	"expire_date"
);
CREATE INDEX IF NOT EXISTS "libraryv2_bookissue_book_id_fcc7ef6e" ON "libraryv2_bookissue" (
	"book_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_bookissue_student_id_515cdfb2" ON "libraryv2_bookissue" (
	"student_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_requestbook_catergory_id_12016a5c" ON "libraryv2_requestbook" (
	"catergory_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_requestbook_yourname_id_648a008b" ON "libraryv2_requestbook" (
	"yourname_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_librarian_user_id_73925890" ON "libraryv2_librarian" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_person_user_id_f56e97ab" ON "libraryv2_person" (
	"user_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_book_catergory_id_f4996b83" ON "libraryv2_book" (
	"catergory_id"
);
CREATE INDEX IF NOT EXISTS "libraryv2_book_formatt_id_c13efaae" ON "libraryv2_book" (
	"formatt_id"
);
COMMIT;
