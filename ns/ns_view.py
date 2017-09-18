from flask import Blueprint, Response, send_from_directory
import requests
from xml.etree import ElementTree
from utils.xmlDictConfig import XmlDictConfig
import simplejson
import os

ns_blueprint = Blueprint('ns', __name__)

@ns_blueprint.route('/ns', methods=['GET'])
def ns_stations():
    response = ns_api('http://webservices.ns.nl/ns-api-stations-v2')
    return Response(simplejson.dumps(response), mimetype='application/json')


@ns_blueprint.route('/ns/<from_station>/<to_station>', methods=['GET'])
def ns_planner(from_station, to_station):
    response = ns_api('http://webservices.ns.nl' +
                      '/ns-api-treinplanner?fromStation=' +
                      from_station +
                      '&toStation=' +
                      to_station)
    return Response(simplejson.dumps(response), mimetype='application/json')


def ns_api(url):
    response = requests.get(url,
                            auth=requests.auth.HTTPBasicAuth(
                                os.getenv('NS_USER'),
                                os.getenv('NS_PASS'))
                            )
    root = ElementTree.XML(response.content)
    return XmlDictConfig(root)
