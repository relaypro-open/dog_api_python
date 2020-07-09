#!/usr/bin/env python
# -*- coding: utf-8 -*-
#from api import get_client
from api import DogClient
import sys, os
import json
import copy
from pprint import pprint

client = DogClient( base_url="http://dog-ubuntu-server.lxd:7070/api")
groups = { group.get("id"):group.get("name") for group in client.get_all_groups()}
zones = { zone.get("id"):zone.get("name") for zone in client.get_all_zones()}

def get_link_name():
    links = client.get_all_links()
    name = links[0].get("name")
    return name

OTHER_ENV=get_link_name()

def update_profile(id):
    profile = client.get_profile(id)
    name = profile.get("name")
    rules = profile.get("rules")
    new_rules = {}
    new_rules_count = 0
    for direction in ["inbound", "outbound"]:
        new_rules[direction] = [] 
        ruleset = rules.get(direction)
        for rule in ruleset:
            #print(rule)
            group = rule.get("group")
            group_type = rule.get("group_type")
            #get rid of unused, confusing "environments"
            try:
                rule.pop("environments")
            except:
                pass
            #tag rule's comment with new link name to indicate it's been duplicated
            rule_comment = rule.get("comment")
            new_rule_needed = False
            if group_type in ["ROLE","ZONE"]:
                if rule.get("comment").count(f"#{OTHER_ENV}_duplicated"):
                    new_rules[direction].append(rule)
                else:
                    rule["comment"] = f"#{OTHER_ENV}_duplicated " + rule.get("comment")
                    new_rules[direction].append(rule)
                    new_rule_needed = True
            external_rule = copy.copy(rule)
            external_rule["environment"] = OTHER_ENV
            if rule.get("environment"): #don't create a new rule if already an exteral rule
                pass
            elif new_rule_needed == False:
                pass
            else:
                if group_type == "ROLE":
                    group_name = groups.get(group)
                    external_rule["group"] = group_name
                    external_rule["comment"] = f"#{OTHER_ENV}_copy " + rule_comment
                    new_rules[direction].append(external_rule)
                    new_rules_count+=1
                elif group_type == "ZONE":
                    group_name = zones.get(group)
                    external_rule["group"] = group_name
                    external_rule["comment"] = f"#{OTHER_ENV}_copy " + rule_comment
                    new_rules[direction].append(external_rule)
                    new_rules_count+=1
            #print(external_rule)
    id = profile.pop("id")
    profile["rules"] = new_rules
    #print(profile)
    if new_rules_count > 0:
        return client.update_profile(id,profile)
    else:
        return f"{id}: NO NEW RULES - PROFILE NOT UPDATED"

def main(argv, stdout, environ):
    print(f"OTHER_ENV: {OTHER_ENV}")
    #profiles = client.get_all_profiles()
    #for p in profiles:
    #    id = p.get("id")
    #    print(id)
    #    new_profile = update_profile(id)
    #    print(new_profile)
    #    break
    profile_id = argv[1]
    print(update_profile(profile_id))

if __name__ == "__main__":
    main(sys.argv, sys.stdout, os.environ)
