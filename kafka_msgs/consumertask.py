"""
 Copyright 2015-2018 IBM

 Licensed under the Apache License, Version 2.0 (the "License");
 you may not use this file except in compliance with the License.
 You may obtain a copy of the License at

 http://www.apache.org/licenses/LICENSE-2.0

 Unless required by applicable law or agreed to in writing, software
 distributed under the License is distributed on an "AS IS" BASIS,
 WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 See the License for the specific language governing permissions and
 limitations under the License.

 Licensed Materials - Property of IBM
 © Copyright IBM Corp. 2015-2018
"""
import asyncio
from time import process_time_ns
from confluent_kafka import Consumer
from pprint import pprint
import json
import sevone_operation as sevone
import swagger_client
from swagger_client.rest import ApiException

class ConsumerTask(object):

    def __init__(self, conf, topic_name, username, password):
        self.consumer = Consumer(conf)
        self.topic_name = topic_name
        self.running = True
        self.username = username
        self.password = password

    def stop(self):
        self.running = False

    @asyncio.coroutine
    def run(self):
        print('The consumer has started')
        self.consumer.subscribe([self.topic_name])
        while self.running:
            msg = self.consumer.poll(1)
            if msg is not None and msg.error() is None:
                pprint("Message consumed: offset={0}, value={1}".format(
                    msg.offset(),
                    msg.value()))
                received_data = json.loads(msg.value().decode())
                configuration = swagger_client.Configuration()
                # Sign In Request
                api_response = sevone.sign_in.SignIn(name=self.username, password=self.password).request()
                # Create Device Request
                request = sevone.create_device.CreateDevice(device_name=received_data['hostname'],token=api_response.token).request()
            else:
                print('No messages consumed')
                yield from asyncio.sleep(2)
        self.consumer.unsubscribe()
        self.consumer.close()
        
