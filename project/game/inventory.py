"""Inventory system for managing player equipment"""
from dataclasses import dataclass
from typing import Optional

@dataclass
class Equipment:
    name: str
    slot: str
    protection: float = 0.0
    durability: float = 100.0

class PlayerInventory:
    def __init__(self):
        self.slots = {
            'helmet': None,
            'headphones': None,
            'facemask': None,
            'tactical_rig': None,
            'backpack': None,
            'weapon_1': None,
            'weapon_2': None,
            'handgun': None,
            'melee': None,
            'arm_armor': None,
            'leg_armor': None
        }
    
    def equip(self, item: Equipment) -> bool:
        """Equip an item in its designated slot"""
        if item.slot in self.slots:
            self.slots[item.slot] = item
            return True
        return False
    
    def unequip(self, slot: str) -> Optional[Equipment]:
        """Remove item from specified slot"""
        if slot in self.slots:
            item = self.slots[slot]
            self.slots[slot] = None
            return item
        return None
    
    def get_equipped(self, slot: str) -> Optional[Equipment]:
        """Get item in specified slot"""
        return self.slots.get(slot)
