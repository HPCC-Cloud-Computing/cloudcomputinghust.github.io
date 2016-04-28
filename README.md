[cloudcomputinghust.github.io](http://cloudcomputinghust.github.io/)  is the official blog of **Cloud Computing Hust**

## Why have 2 branch?
- manager: Branch for manager content by MARKDOWN
- master: Branch for show content by HTML => [Website](http://cloudcomputinghust.github.io/)

```
git clone --recursive --branch manager git@github.com:cloudcomputinghust/cloudcomputinghust.github.io.git ~/cloud
git submodule foreach  git checkout master
cd ~/cloud
```
## How to write new content?

```
content/
.
└── 2016
	|── cai-dat-keystone-to-keystone-federation.html
	└── mo-hinh-hoat-dong-federation.html
```
#### Create new content
```
vi content/bai-viet-moi.md
```

#### Run server and review

```
make devserver
```
- Website is avaible at [127.0.0.1:8000](http://127.0.0.1:8000)

#### Shutdown server
```
make stopserver
```

#### Deploy new content
```

# push html to master branch
make html
cd output
git add *
git commit -m 'add new content.html'
git push origin master

# push markdown to manager branch
cd -
git commit -a -m 'add content/content/bai-viet-moi.md'
git push origin manager
```
`
`
