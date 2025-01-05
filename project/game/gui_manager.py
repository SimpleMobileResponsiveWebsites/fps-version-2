"""GUI manager for displaying player equipment and status"""
from direct.gui.OnscreenText import OnscreenText
from direct.gui.DirectFrame import DirectFrame
from panda3d.core import TextNode, Point3
from .inventory import PlayerInventory

class EquipmentGUI:
    def __init__(self, game):
        self.game = game
        self.setup_equipment_display()
    
    def setup_equipment_display(self):
        """Create the equipment display frame"""
        # Create main frame
        self.frame = DirectFrame(
            frameColor=(0, 0, 0, 0.7),
            frameSize=(-0.3, 0.3, -0.4, 0.4),
            pos=(1.1, 0, 0)  # Right side of screen
        )
        
        # Equipment slot labels
        self.slot_labels = {}
        self.status_labels = {}
        
        slots = [
            ('helmet', 'Helmet'),
            ('headphones', 'Headphones'),
            ('facemask', 'Face Mask'),
            ('tactical_rig', 'Tactical Rig'),
            ('backpack', 'Backpack'),
            ('weapon_1', 'Primary Weapon'),
            ('weapon_2', 'Secondary Weapon'),
            ('handgun', 'Handgun'),
            ('melee', 'Melee Weapon'),
            ('arm_armor', 'Arm Armor'),
            ('leg_armor', 'Leg Armor')
        ]
        
        for i, (slot_id, slot_name) in enumerate(slots):
            y_pos = 0.35 - (i * 0.07)
            
            # Slot label
            self.slot_labels[slot_id] = OnscreenText(
                text=f"{slot_name}:",
                pos=(-0.25, y_pos),
                scale=0.04,
                fg=(1, 1, 1, 1),
                align=TextNode.ALeft,
                parent=self.frame
            )
            
            # Status label (empty/equipped item name)
            self.status_labels[slot_id] = OnscreenText(
                text="Empty",
                pos=(0.1, y_pos),
                scale=0.04,
                fg=(0.7, 0.7, 0.7, 1),
                align=TextNode.ALeft,
                parent=self.frame
            )
    
    def update_equipment_display(self, inventory: PlayerInventory):
        """Update the equipment display with current inventory"""
        for slot in inventory.slots:
            item = inventory.get_equipped(slot)
            if item:
                self.status_labels[slot].setText(item.name)
                self.status_labels[slot].setFg((0, 1, 0, 1))  # Green for equipped
            else:
                self.status_labels[slot].setText("Empty")
                self.status_labels[slot].setFg((0.7, 0.7, 0.7, 1))  # Gray for empty
