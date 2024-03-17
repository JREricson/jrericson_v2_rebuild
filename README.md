# jrericson_v2_rebuild
### [https://jrericson.com](https://jrericson.com)

## Project summary
 It currently serves as a portfolio to show code samples and showcase projects that I have been working on. The reason behind the technology used is described in the sections that follow.


 ![site home](https://raw.githubusercontent.com/JREricson/jrericson_v2_rebuild/main/documentation/cover_photo.png)

## Project goals

The primary goal was to create a functional portfolio following "good coding practices." In addition, it was to gain more experience with the technology used (Django, Docker, Linode, Postgres, etch). Much of it will be used in other projects. I could have built much of the site in a simpler way. For example, building in React, hosting on Netlify, or manually entering pages instead using a database and markdown.

## Technology
Python, Django, markdown, nginx, Docker, Docker-compose, Linode, bash, boostrap, Linux, SSH, Rsync.

 ![tech img](https://raw.githubusercontent.com/JREricson/jrericson_v2_rebuild/main/documentation/tech.png)

## Key Features
- Live website with https through Letsencrypt certificate authority
- S3 storage
- Database backups
- Deployment through remote Linux server
- Docker Container based deployment and development
- Email based contact form (depreciated)
  
## Coding style

For personal projects, I like to write code where the variable names are descriptive enough to tell a programmer not familiar with the language enough of what is going on. Comments are kept to a minimum and only included where explaining something that would not be clear. There are many additional `# TODO` comments here, but I prefer to avoid having as  many in production.


## Site structure



### Projects Model

Projects are stored a variety of attributes, such as ranking (used for ordering), a git hub link, a sample image, and a description of the project.

Descriptions are added through the admin console as markdown, which is converted to HTML though a "markdownify`" filter in the UI. This makes adding project description easier and allows me to use similar descriptions as the Github readmes with little modification.

![markdown ex](https://raw.githubusercontent.com/JREricson/jrericson_v2_rebuild/main/documentation/markup_description.png)


Projects are displayed and paginated through a Django `Listview`. Project descriptions are displayed using through a Django `Detailview`.

## Security 

- **Firewall**: Using ufw to further restrict access to site.
  
  ![](https://raw.githubusercontent.com/JREricson/jrericson_v2_rebuild/main/documentation/ufw%20status.png)
- **SSH key**: Access to host is restricted through SSH key. Password and root access is disabled.
- **One way access to S3 buckets** - The system is only able to write to S3 buckets, ensuring that no data can be over written.
- **Cors**: For trusted origins in Django.
- **Hidden access points**: The Admin portal is accessed via a hidden location.
- **HTTPS**: Using Letsencrypt certificate authority.
   ![](https://raw.githubusercontent.com/JREricson/jrericson_v2_rebuild/main/documentation/secure_dns.png)
- **Other standard Practices:** Including sanitation, `.env` files, and `.gitignore` files.



## Backups
The Application uses "django-dbbackup" which provides a wrapper over Postgres's `pg_dump`. Backups are currently run manually after updating content. A previous version of the site used **cron jobs**. It is possible that I will automate it with Celery in the future. All backups are stored externally in an S3 Bucket as described below.

Linode offers backup services, which I am not paying for. Restoring the system would be as easy as starting the Docker image, running migrations and similar operations, then and using the command in django-dbbackup to restore the data base. This allows allows for easier portability if I want to run locally or on a different site.


## S3 storage

S3 is utilized to store all backups. The site is set up to store other content there if desired for future additions to the site or in similar sites that share the same reusable structure.


## Database: PostgresSQL

PostgresSQL was chosen as I am most familiar with this favor of SQL and it is a free option.


## UI
Bootstrap was chosen for simplicity. The "Darkly" theme from Bootswatch to make the site less like generic bootstrap. I prefer dark themes for my eyes. Because it is my site, it will not have a light theme.

## Site hosting 

An Ubuntu server (LTS) was chosen as I am familiar with Debian distributions.

Remote access is done through SSH or with the "Visual Studio Code Remote - SSH" extension. Files are transferred using Rsync

## Docker and Docker-compose

Docker has been chosen for the following reasons.

1. It simplifies porting from Development to Production.
2. It makes it easier to run the Nginx server, the database, the certificate authority and other services with one another.

Docker compose simplifies the process even further. 

Separate Docker/Docker-compose files are provided for the production and local development environments.

## Nginx Webserver
Nginx is used to host static content and the site as a reverse proxy.


## Email Form
I previously had `send_mail()` send emails to my primary address. However, Google is discontinuing password based logins. I will likely switch to OAuth based tokens for email when I find the time. Right now, the contact page redirects to my Linked in page.


## Git Usage

I use branching similar to the [git_flow](https://www.atlassian.com/git/tutorials/comparing-workflows/gitflow-workflow#:~:text=What%20is%20Gitflow%3F,by%20Vincent%20Driessen%20at%20nvie.) method. There is a production branch and a development branch for features that get pushed into it.


## Simplifying development

An `aliases.sh` Bash script file is loaded to create shortcuts for common commands specific to the project, that I do not want to include in my personal `.bash_aliases` file.



## Citations on codebase
The structure and design choice for the site were heavily based on the following sources. Much of the code from those tutorials was used as boiler plate

- https://testdriven.io/blog/dockerizing-django-with-postgres-gunicorn-and-nginx/
- https://testdriven.io/blog/storing-django-static-and-media-files-on-amazon-s3/



