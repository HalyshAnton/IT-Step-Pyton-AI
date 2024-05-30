import redis


r = redis.Redis(host='localhost', port=6379, db=0, decode_responses=True)

r.set('user:name', 'Alice')
name = r.get('user:name')
# print(name)
# print(type(name))

r.set('user:age', 7)
age = r.get('user:age')
# print(age)
# print(type(age))

# r.decr
r.incr('user:age', 10)
age = r.get('user:age')
# r.incrby()
# print(age)
# print(type(age))

r.geoadd('cities', (30.14, 50.25, 'Kyiv'))
r.geoadd('cities', (10.58, 65.0, 'London'))

pos = r.geopos('cities', 'Kyiv', 'London')
# print(pos)
# print(type(pos[0][0]))

dist = r.geodist('cities', 'Kyiv', 'London', 'km')
# print(dist)
# print(type(dist))
r.delete('items')
r.rpush('items', 1, 2, 3)
items = r.lrange('items', 0, -1)
# print(items, type(items))
r.delete('items')

r.sadd('items', 1, 2, 3)
items = r.smembers('items')
# print(items, type(items))
r.delete('items')

r.hset('items', 'name', 'Alice')
r.hset('items', 'age', 12)

r.hset('items', mapping={'ghjh': 2123, "ghjgjh": 'hjkj'})

items = r.hgetall('items')
print(items)
print(type(items))
