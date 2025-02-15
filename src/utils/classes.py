import discord
from discord import app_commands
from discord.ext import commands

class Persistent_view(discord.ui.View):
    def __init__(self, btn_dict: dict[str, discord.Embed]):
        super().__init__(timeout=None)
        self.btn_dict = btn_dict
        
        for name, embed in btn_dict.items():
            btn = discord.ui.Button(label=name, custom_id=f"button_{name.lower()}")
            self.add_item(btn)
    
    async def interaction_check(self, interaction: discord.Interaction) -> bool:
        custom_id = interaction.data["custom_id"]
        button_name = custom_id.replace("button_", "").title()
        
        if button_name in self.btn_dict:
            await interaction.response.send_message(
                embed=self.btn_dict[button_name], 
                ephemeral=True
            )
        return True


class Super_bot(commands.Bot):
    def __init__(self):
        super().__init__(command_prefix="pk!", intents=discord.Intents.all())
    
    async def setup_hook(self):
        from src.commands.about_bot import categories
        self.add_view(Persistent_view(categories))
