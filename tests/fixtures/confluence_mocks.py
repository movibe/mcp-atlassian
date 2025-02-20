MOCK_CQL_SEARCH_RESPONSE = {
    'results': [{
        'content': {
            'id': '123456789',
            'type': 'page',
            'status': 'current',
            'title': '2024-01-01: Team Progress Meeting 01',
            'childTypes': {},
            'macroRenderedOutput': {},
            'restrictions': {},
            '_expandable': {
                'container': '',
                'metadata': '',
                'extensions': '',
                'operations': '',
                'children': '',
                'history': '/rest/api/content/123456789/history',
                'ancestors': '',
                'body': '',
                'version': '',
                'descendants': '',
                'space': '/rest/api/space/TEAM'
            },
            '_links': {
                'webui': '/spaces/TEAM/pages/123456789/2024-01-01+Team+Progress+Meeting+01',
                'self': 'https://example.atlassian.net/wiki/rest/api/content/123456789',
                'tinyui': '/x/ABC123'
            }
        },
        'title': '2024-01-01: Team Progress Meeting 01',
        'excerpt': '📅 Date\n2024-01-01\n👥 Participants\nJohn Smith\nJane Doe\nBob Wilson\n!-@123456',
        'url': '/spaces/TEAM/pages/123456789/2024-01-01+Team+Progress+Meeting+01',
        'resultGlobalContainer': {
            'title': 'Team Space',
            'displayUrl': '/spaces/TEAM'
        },
        'breadcrumbs': [],
        'entityType': 'content',
        'iconCssClass': 'aui-icon content-type-page',
        'lastModified': '2024-01-01T08:00:00.000Z',
        'friendlyLastModified': 'Jan 01, 2024',
        'score': 0.0
    }],
    'start': 0,
    'limit': 50,
    'size': 1,
    'totalSize': 1,
    'cqlQuery': 'parent = 123456789',
    'searchDuration': 156,
    '_links': {
        'base': 'https://example.atlassian.net/wiki',
        'context': '/wiki',
        'self': 'https://example.atlassian.net/wiki/rest/api/search?cql=parent%3D123456789'
    }
}

MOCK_PAGE_RESPONSE = {
    'id': '987654321',
    'type': 'page',
    'status': 'current',
    'title': 'Example Meeting Notes',
    'space': {
        'id': 11111111,
        'key': 'PROJ',
        'alias': 'PROJ',
        'name': 'Project Space',
        'type': 'global',
        'status': 'current',
        '_expandable': {
            'settings': '/rest/api/space/PROJ/settings',
            'metadata': '',
            'operations': '',
            'lookAndFeel': '/rest/api/settings/lookandfeel?spaceKey=PROJ',
            'identifiers': '',
            'permissions': '',
            'roles': '',
            'icon': '',
            'description': '',
            'theme': '/rest/api/space/PROJ/theme',
            'history': '',
            'homepage': '/rest/api/content/11111111'
        },
        '_links': {
            'webui': '/spaces/PROJ',
            'self': 'https://example.atlassian.net/wiki/rest/api/space/PROJ'
        }
    },
    'version': {
        'by': {
            'type': 'known',
            'accountId': 'user123',
            'accountType': 'atlassian',
            'email': '',
            'publicName': 'Example User (Unlicensed)',
            'profilePicture': {
                'path': '/wiki/aa-avatar/user123',
                'width': 48,
                'height': 48,
                'isDefault': False
            },
            'displayName': 'Example User (Unlicensed)',
            'isExternalCollaborator': False,
            'isGuest': False,
            'locale': 'en_US',
            'accountStatus': 'active',
            '_expandable': {
                'operations': '',
                'personalSpace': ''
            },
            '_links': {
                'self': 'https://example.atlassian.net/wiki/rest/api/user?accountId=user123'
            }
        },
        'when': '2024-01-01T09:00:00.000Z',
        'friendlyWhen': 'Jan 01, 2024',
        'message': '',
        'number': 1,
        'minorEdit': False,
        'ncsStepVersion': '1234',
        'ncsStepVersionSource': 'ncs-ack',
        'confRev': 'confluence$content$987654321.1',
        'contentTypeModified': False,
        '_expandable': {
            'collaborators': '',
            'content': '/rest/api/content/987654321'
        },
        '_links': {
            'self': 'https://example.atlassian.net/wiki/rest/api/content/987654321/version/1'
        }
    },
    'body': {
        'storage': {
            'value': '<h2><ac:emoticon ac:name="blue-star" />&nbsp;Date</h2><p><time datetime="2024-01-01" /></p><h2><ac:emoticon ac:name="blue-star" />&nbsp;Participants</h2><ul><li><p><ac:link><ri:user ri:account-id="user123" /></ac:link></p></li></ul><h2><ac:emoticon ac:name="blue-star" />&nbsp;Goals</h2><ul><li><p>Example goal</p></li></ul>',
            'representation': 'storage',
            'embeddedContent': [],
            '_expandable': {
                'content': '/rest/api/content/987654321'
            }
        },
        '_expandable': {
            'editor': '',
            'atlas_doc_format': '',
            'view': '',
            'export_view': '',
            'styled_view': '',
            'dynamic': '',
            'editor2': '',
            'anonymous_export_view': ''
        }
    },
    'macroRenderedOutput': {},
    'extensions': {
        'position': 123456789
    },
    '_expandable': {
        'childTypes': '',
        'container': '/rest/api/space/PROJ',
        'schedulePublishInfo': '',
        'metadata': '',
        'operations': '',
        'schedulePublishDate': '',
        'children': '/rest/api/content/987654321/child',
        'restrictions': '/rest/api/content/987654321/restriction/byOperation',
        'history': '/rest/api/content/987654321/history',
        'ancestors': '',
        'descendants': '/rest/api/content/987654321/descendant'
    },
    '_links': {
        'editui': '/pages/resumedraft.action?draftId=987654321',
        'webui': '/spaces/PROJ/pages/987654321/Example+Meeting+Notes',
        'edituiv2': '/spaces/PROJ/pages/edit-v2/987654321',
        'context': '/wiki',
        'self': 'https://example.atlassian.net/wiki/rest/api/content/987654321',
        'tinyui': '/x/AbCdE',
        'collection': '/rest/api/content',
        'base': 'https://example.atlassian.net/wiki'
    }
}


MOCK_COMMENTS_RESPONSE = {
    'results': [{
        'id': '456789123',
        'type': 'comment',
        'status': 'current',
        'title': 'Re: Technical Design Document',
        'version': {
            'by': {
                'type': 'known',
                'accountId': '712020:abc123-def456-ghi789',
                'accountType': 'atlassian',
                'email': '',
                'publicName': 'John Doe',
                'profilePicture': {
                    'path': '/wiki/aa-avatar/712020:abc123-def456-ghi789',
                    'width': 48,
                    'height': 48,
                    'isDefault': False
                },
                'displayName': 'John Doe',
                'isExternalCollaborator': False,
                'isGuest': False,
                'locale': 'en_US',
                'accountStatus': 'active',
                '_expandable': {
                    'operations': '',
                    'personalSpace': ''
                },
                '_links': {
                    'self': 'https://company.atlassian.net/wiki/rest/api/user?accountId=712020:abc123-def456-ghi789'
                }
            },
            'when': '2024-01-01T10:00:00.000Z',
            'friendlyWhen': 'Jan 1, 2024',
            'message': '',
            'number': 1,
            'minorEdit': False,
            'contentTypeModified': False,
            '_expandable': {
                'collaborators': '',
                'content': '/rest/api/content/456789123'
            },
            '_links': {
                'self': 'https://company.atlassian.net/wiki/rest/api/content/456789123/version/1'
            }
        },
        'macroRenderedOutput': {},
        'body': {
            'view': {
                'value': '<p>Comment content here</p>',
                'representation': 'view',
                '_expandable': {
                    'webresource': '',
                    'embeddedContent': '',
                    'mediaToken': '',
                    'content': '/rest/api/content/456789123'
                }
            },
            '_expandable': {
                'editor': '',
                'atlas_doc_format': '',
                'export_view': '',
                'styled_view': '',
                'dynamic': '',
                'storage': '',
                'editor2': '',
                'anonymous_export_view': ''
            }
        },
        'extensions': {
            'location': 'inline',
            '_expandable': {
                'inlineProperties': '',
                'resolution': ''
            }
        },
        '_expandable': {
            'childTypes': '',
            'container': '/rest/api/content/123456789',
            'schedulePublishInfo': '',
            'metadata': '',
            'operations': '',
            'schedulePublishDate': '',
            'children': '/rest/api/content/456789123/child',
            'restrictions': '/rest/api/content/456789123/restriction/byOperation',
            'history': '/rest/api/content/456789123/history',
            'ancestors': '',
            'descendants': '/rest/api/content/456789123/descendant',
            'space': '/rest/api/space/TEAM'
        },
        '_links': {
            'webui': '/spaces/TEAM/pages/123456789/Technical+Design+Document?focusedCommentId=456789123',
            'self': 'https://company.atlassian.net/wiki/rest/api/content/456789123'
        }
    }]
}
MOCK_SPACES_RESPONSE = {
    'results': [
        {
            'id': 11111111,
            'key': '~user1',
            'alias': '~user1',
            'name': 'User One',
            'type': 'personal',
            'status': 'archived',
            '_expandable': {
                'settings': '/rest/api/space/~user1/settings',
                'metadata': '',
                'operations': '',
                'lookAndFeel': '/rest/api/settings/lookandfeel?spaceKey=~user1',
                'identifiers': '',
                'permissions': '',
                'roles': '',
                'icon': '',
                'description': '',
                'theme': '/rest/api/space/~user1/theme',
                'history': '',
                'homepage': '/rest/api/content/11111112'
            },
            '_links': {
                'webui': '/spaces/~user1',
                'self': 'https://example.atlassian.net/wiki/rest/api/space/~user1'
            }
        },
        {
            'id': 22222222,
            'key': 'PROJ',
            'alias': 'PROJ',
            'name': 'Project Space',
            'type': 'global',
            'status': 'current',
            '_expandable': {
                'settings': '/rest/api/space/PROJ/settings',
                'metadata': '',
                'operations': '',
                'lookAndFeel': '/rest/api/settings/lookandfeel?spaceKey=PROJ',
                'identifiers': '',
                'permissions': '',
                'roles': '',
                'icon': '',
                'description': '',
                'theme': '/rest/api/space/PROJ/theme',
                'history': '',
                'homepage': '/rest/api/content/22222223'
            },
            '_links': {
                'webui': '/spaces/PROJ',
                'self': 'https://example.atlassian.net/wiki/rest/api/space/PROJ'
            }
        }
    ],
    'start': 0,
    'limit': 5,
    'size': 2,
    '_links': {
        'base': 'https://example.atlassian.net/wiki',
        'context': '/wiki',
        'next': '/rest/api/space?next=true&limit=5&start=5',
        'self': 'https://example.atlassian.net/wiki/rest/api/space'
    }
}

MOCK_PAGES_FROM_SPACE_RESPONSE = [{
    'id': '123456789',
    'type': 'page',
    'status': 'current',
    'title': 'Sample Research Paper Title',
    'macroRenderedOutput': {},
    'body': {
        'storage': {
            'value': '<h3>[Date]</h3><p><em>Result</em>: Sample Result</p><p><em>Reviews</em>: </p><p>Sample content with various formatting</p>',
            'representation': 'storage',
            'embeddedContent': [],
            '_expandable': {'content': '/rest/api/content/123456789'}
        },
        '_expandable': {
            'editor': '',
            'atlas_doc_format': '',
            'view': '',
            'export_view': '',
            'styled_view': '',
            'dynamic': '',
            'editor2': '',
            'anonymous_export_view': ''
        }
    },
    'extensions': {'position': 12345},
    '_expandable': {
        'container': '/rest/api/space/PROJ',
        'metadata': '',
        'restrictions': '/rest/api/content/123456789/restriction/byOperation',
        'history': '/rest/api/content/123456789/history',
        'version': '',
        'descendants': '/rest/api/content/123456789/descendant',
        'space': '/rest/api/space/PROJ',
        'childTypes': '',
        'schedulePublishInfo': '',
        'operations': '',
        'schedulePublishDate': '',
        'children': '/rest/api/content/123456789/child',
        'ancestors': ''
    },
    '_links': {
        'self': 'https://example.atlassian.net/wiki/rest/api/content/123456789',
        'tinyui': '/x/ABC123',
        'editui': '/pages/resumedraft.action?draftId=123456789',
        'webui': '/spaces/PROJ/pages/123456789/Sample+Research+Paper+Title',
        'edituiv2': '/spaces/PROJ/pages/edit-v2/123456789'
    }
}]
