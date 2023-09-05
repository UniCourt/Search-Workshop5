## Do the following to run regression test.

1. Bring postgres service up from Search-Workshop1
```
cd Search-Workshop1
docker-compose up
```

2. Bring elasticsearch and kibana services up from Search-Workshop2
```
cd Search-Workshop2
docker-compose up
```

3. Bring APIs up from Search-Workshop3
```
cd Search-Workshop3
docker build -t ws3 .
docker run -p 5000:5000 "ws3:latest"
```

4. Run regression tests.\
Before building the docker image, update environment variable API_HOST to your local ip.
```
cd Search-Workshop5
docker build -t ws5 .
docker run -it "ws5:latest" sh
python -m pytest
```
