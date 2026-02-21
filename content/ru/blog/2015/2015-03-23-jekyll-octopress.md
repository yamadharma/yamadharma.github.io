---
categories:
  - sysadmin
date: 2015-03-23T13:51:36+03:00
lang: ru
slug: jekyll-octopress
tags:
  - jekyll
title: Перенос блога на Jekyll + Octopress
projects: ["misc-utils"]
---


## Репозиторий для сайта

- Создал локальный каталог для сайта:

```bash
mkdir ~/mysite
```

<!--more-->

## Локальный git-репозиторий

- Создал пустой git-репозиторий:

```bash
cd ~/mysite
git init
```

- Создал в нём файл `README.md`

```bash
touch README.md
``

- Сделал коммит:

```bash
git add .
git commit -am 'Initial commit'
```

- Создаю ветку для кода (в `master` будет сайт):

```bash
git branch source
git checkout source
```

[Далее создаю шаблон для сайта](##head_site-template-create) в ветке `source`.


#### Репозиторий на Bitbucket ######

Я пользовался [инструкцией от bitbucket'а][website-on-bitbucket].

- Создал на bitbucket'е репозиторий с названием
`yamadharma.bitbucket.org`.

- Выложил репозиторий

```bash
cd ~/mysite
git remote add origin git@bitbucket.org:yamadharma/yamadharma.bitbucket.org.git
git push -u origin --all
git push -u origin --tags
```

## Выкладывание сайта на Bitbucket

- Создал файл `_deploy.yml` с помощью команды

```bash
octopress deploy init git -u git@bitbucket.org:yamadharma/yamadharma.bitbucket.org.git
```

- Подредактировал `.gitignore`:

```bash
echo ".deploy" >> .gitignore
```

- Сгенерил сайт:

```bash
jekyll b
```

- Выложил существующий сайт:

```bash
octopress deploy
```

- Положил ветку `source` на git:

```bash
git add .
git commit -am 'Поправил сайт'
git push
```

## <a name='head_site-template-create'></a> Создание шаблона сайта ####

- В каталоге сайта создаю шаблон:

```bash
cd ~/mysite
git checkout source
octopress new -f .
```

[website-on-bitbucket]: https://confluence.atlassian.com/display/BITBUCKET/Publishing+a+Website+on+Bitbucket

