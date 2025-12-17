# Ai/smapi_ki.py
# SMAPI-KI Core v0.3 - Python Version

class SMAPI_KI:
    @staticmethod
    def process(input_text: str) -> str:
        text = input_text.lower()

        if "morgen" in text or "start" in text:
            return SMAPI_KI.generate_morning_message_mod()
        elif "json" in text or "content patcher" in text:
            return SMAPI_KI.generate_content_patcher()
        elif "npc" in text:
            return SMAPI_KI.generate_npc_mod()
        else:
            return ("Ich habe deine Anfrage verstanden, aber noch keine Regel dafür.\n\n"
                    "Tipps für Tests:\n- 'morgen nachricht'\n- 'content patcher json'\n- 'erstelle npc'")

    @staticmethod
    def generate_morning_message_mod() -> str:
        return '''// Beispiel SMAPI Mod (C#)
using StardewModdingAPI;
using StardewValley;

public class ModEntry : Mod
{
    public override void Entry(IModHelper helper)
    {
        helper.Events.GameLoop.DayStarted += OnDayStarted;
    }

    private void OnDayStarted(object sender, StardewModdingAPI.Events.DayStartedEventArgs e)
    {
        Game1.addHUDMessage(new HUDMessage("Guten Morgen von deiner SMAPI‑KI!", 2));
    }
}'''

    @staticmethod
    def generate_content_patcher() -> str:
        return '''// content.json (Content Patcher)
{
  "Format": "1.30.0",
  "Changes": [
    {
      "Action": "EditData",
      "Target": "Data\\Mail",
      "Entries": {
        "SMAPI_KI_Test": "Hallo! Diese Nachricht kommt von deiner Offline‑SMAPI‑KI."
      }
    }
  ]
}'''

    @staticmethod
    def generate_npc_mod() -> str:
        return '''// Beispiel SMAPI Mod (NPC erstellen)
using StardewModdingAPI;
using StardewValley;

public class NPCModEntry : Mod
{
    public override void Entry(IModHelper helper)
    {
        helper.ConsoleCommands.Add("spawn_npc", "Spawnt einen Beispiel-NPC", this.SpawnNPC);
    }

    private void SpawnNPC(string command, string[] args)
    {
        // Beispiel-NPC Logik
        Game1.showGlobalMessage("Ein neuer NPC wurde erstellt!");
    }
}'''


# Beispiel Testlauf
if __name__ == "__main__":
    user_input = input("Was soll die KI erstellen? ")
    output = SMAPI_KI.process(user_input)
    print("\n--- KI OUTPUT ---\n")
    print(output)
