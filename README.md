
### 打包成镜像步骤：
```
# 1、将依赖都写入 requirements.txt
pip freeze > requirements.txt

# 2、创建dockerfile文件，写入build步骤

# 3、build
docker build -t demo:v1 .

```

### 运行步骤
```
# 1、创建一个空目录，并在该目录下创建文件 application.yml，并进行相应的配置

# 2、在application.yml所在目录下运行容器
docker run --name health -e TZ=Asia/Shanghai -v %cd%\application.yml:/application.yml -ti -d demo:v1

```