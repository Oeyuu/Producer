import sys
from kafka import KafkaProducer

# Die Argumente für bootstrap_servers und topic
# servers = sys.argv[0]
# topic = sys.argv[1]
# password = sys.argv[2]

# print(servers)
# print(topic)
#bootstrap_servers=["b-3-public.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9196","b-1-public.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9196","b-2-public.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9196"],
# bootstrap_servers=["b-3.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9096","b-2.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9096","b-1.mskcluster.xns45o.c8.kafka.eu-central-1.amazonaws.com:9096"],


# Erstelle den Kafka-Producer
producer = KafkaProducer(
    security_protocol="SASL_SSL",
    sasl_mechanism="SCRAM-SHA-512",
    sasl_plain_username="super_user",
    sasl_plain_password="DuC8Zx2E@Le1NY2MqkN9",
   bootstrap_servers=["b-2-public.mskcluster.plvcmc.c8.kafka.eu-central-1.amazonaws.com:9196","b-1-public.mskcluster.plvcmc.c8.kafka.eu-central-1.amazonaws.com:9196","b-3-public.mskcluster.plvcmc.c8.kafka.eu-central-1.amazonaws.com:9196"],
)


# Sende Nachrichten
for _ in range(100):
    producer.send("test1", b"some_message_bytes")

producer.flush()
metrics = producer.metrics()


print(producer.config)

# # Block until a single message is sent (or timeout)
# future = producer.send("foobar", b"another_message")
# result = future.get(timeout=60)

# # Use a key for hashed-partitioning
# producer.send("foobar", key=b"foo", value=b"bar")

# Serialize json messages
# import json

# producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode("utf-8"))
# producer.send("fizzbuzz", {"foo": "bar"})


# # Serialize string keys
# producer = KafkaProducer(key_serializer=str.encode)
# producer.send("flipflap", key="ping", value=b"1234")

# # Compress messages
# producer = KafkaProducer(compression_type="gzip")
# for i in range(1000):
#     producer.send("foobar", b"msg %d" % i)

# # Include record headers. The format is list of tuples with string key
# # and bytes value.
# producer.send('foobar', value=b'c29tZSB2YWx1ZQ==', headers=[('content-encoding', b'base64')])
