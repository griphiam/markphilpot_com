Title: Static Blog Publishing To S3
Date: 2016-03-07 18:49:00
Tags: s3, travis, pelican
Category: blog
Slug: static_blog_publishing
Summary: How to publish a static blog
Hero: background-image: url(/images/2016/blog_publish_workflow/hero.jpg);
status: draft

[TOC]

This quick tutorial will take a static blogging engine ([jekyll](https://jekyllrb.com/), [pelican](http://blog.getpelican.com/), [hugo](http://www.gohugo.io/)) and publish it to s3 automatically. I'm making the following assumptions:

* Your static blog is under some sort of source control
* A designated branch in your source control should be published (e.g. master)

In the end you will get a publishing workflow that give you:

* Automatic publishing to S3 when changes are pushed to your master branch
* SSL for your domain (via AWS Cloudfront)

In this example, I'm using [pelican](http://blog.getpelican.com/) for my blog and [travis](https://travis-ci.org/) for my CI. The workflow can definitely be adapted for use with other blogs and other CI services. Travis is free if your blog repository is public in either [Github](https://github.com) or [Bitbucket](https://bitbucket.com).

## Rationale

The main reason *I* wanted to move to this system was really twofold: I wanted a system where I could write and post from an iPad and I wanted to get away from my old rsync as a deployment strategy.

There were a few posts that detailed bits and pieces of this workflow, but nothing that seemed to capture the process from beginning to end.

## Setup AWS

I'm assuming you already have an AWS account.  If you don't, there are plenty of tutorials to get you started. Once you've signed up, head over to the AWS console.

### Create IAM User

For security reasons, we want to create a dedicated user whose sole responsibility is to deploy your blog to an S3 bucket.

Go to the IAM screen and create a new user.  You will want to record your AWS_ACCESS_KEY_ID and AWS_SECRET_KEY values for this user as we will need them later.

### Create &amp; Configure S3 Bucket

First go to the S3 screen and create a bucket for your domain.

## Setup Travis

Sign up for an account and add your blog repository to the list of repositories. In the settings screen, you will want to add environment variables for your AWS key and secret.

In your blog's repository, create a `.travis.yml` file. The following is an example of what it might look like.

```
#!yml hl_lines="14 15 16"
language: python
python:
  - "2.7"
cache:
  - apt
  - pip
install:
  - "pip install -r requirements.txt"
script: "pelican -s publishconf.py content/"
deploy:
  provider: s3
  access_key_id: $AWS_ACCESS_KEY # Env
  secret_access_key: $AWS_SECRET_KEY # Env
  bucket: mydomain.com
  endpoint: mydomain.com.s3-website-us-west-2.amazonaws.com
  region: us-west-2
  skip_cleanup: true
  local-dir: output
  acl: public_read
  detect_encoding: true
  cache_control: "max-age=600"
notifications:
  email:
    on_failure: always
branches:
  only:
    - master
```

You will want to modify the `install` and `script` steps to your static blog's 'generate' step. Also, change the highlighted lines to match your domain and the parameters from your S3 bucket.

## AWS Cloudfront
