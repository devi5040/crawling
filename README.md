# crawling

#If we get error like

> > git pull origin master
> > From https://github.com/devi5040/crawling

- branch master -> FETCH_HEAD
  fatal: refusing to merge unrelated histories

#try with
git pull origin master --allow-unrelated-histories
