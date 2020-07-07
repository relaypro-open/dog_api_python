#!/usr/bin/env python
# -*- coding: utf-8 -*-
from api import get_client
import json
import copy
from pprint import pprint


client = get_client()
groups = { group.get("id"):group.get("name") for group in client.get_all_groups()}
zones = { zone.get("id"):zone.get("name") for zone in client.get_all_zones()}
OTHER_ENV="d2"

profiles = client.get_all_profiles()
for p in profiles:
    id = p.get("id")
    print(id)
    profile = client.get_profile(id)
    name = profile.get("name")
    rules = profile.get("rules")
    new_rules = {}
    for direction in ["inbound", "outbound"]:
        new_rules[direction] = [] 
        ruleset = rules.get(direction)
        for rule in ruleset:
            #print(rule)
            group = rule.get("group")
            group_type = rule.get("group_type")
            rule.pop("order")
            rule.pop("environments")
            if group_type == "ROLE":
                group_name = groups.get(group)
            elif group_type == "ZONE":
                group_name = zones.get(group)
            external_rule = copy.copy(rule)
            external_rule["environment"] = OTHER_ENV
            #print(external_rule)
            new_rules[direction].append(rule)
            new_rules[direction].append(external_rule)
    id = profile.pop("id")
    profile["rules"] = new_rules
    #print(profile)
    print(client.update_profile(id,profile))
    break
