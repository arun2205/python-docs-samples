#!/usr/bin/env python

# Copyright 2019 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

# This sample walks a user through creating a Cloud Dataproc cluster using
# the Python client library.
#
# This script can be run on its own:
#   python create_cluster.py ${PROJECT_ID} ${REGION} ${CLUSTER_NAME}


# [START dataproc_create_cluster]
import sys

from google.cloud import dataproc_v1 as dataproc


def create_cluster(project_id, region, cluster_name):
    """This sample walks a user through creating a Cloud Dataproc cluster
       using the Python client library.

       Args:
           project_id (string): Project to use for creating resources.
           region (string): Region where the resources should live.
           cluster_name (string): Name to use for creating a cluster.
    """

    # Create a client with the endpoint set to the desired cluster region.
    cluster_client = dataproc.ClusterControllerClient(client_options={
        'api_endpoint': '{}-dataproc.googleapis.com:443'.format(region),
        'project_id': project_id
    })

    # Create the cluster config.
    cluster = {
        'project_id': project_id,
        'cluster_name': cluster_name,
        'config': {
            'master_config': {
                'num_instances': 1,
                'machine_type_uri': 'n1-standard-1'
            },
            'worker_config': {
                'num_instances': 2,
                'machine_type_uri': 'n1-standard-1'
            }
        }
    }

    # Create the cluster.
    operation = cluster_client.create_cluster(project_id, region, cluster)
    result = operation.result()

    # Output a success message.
    print('Cluster created successfully: {}'.format(result.cluster_name))


if __name__ == "__main__":
    project_id = sys.argv[1]
    region = sys.argv[2]
    cluster_name = sys.argv[3]
    create_cluster(project_id, region, cluster_name)
# [END dataproc_create_cluster]
