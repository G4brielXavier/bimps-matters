from dataclasses import dataclass

bimps = {
    "name": "BIMPS",
    "version": "0.2.0",
    "creator": "Gabriel Xavier (Dotket)",
    "release": "2024-08-11"
}

@dataclass
class app:
    name: str
    version: str
    creator: str
    release: str
    
appBimps = app(bimps['name'], bimps['version'], bimps['creator'], bimps['release'])