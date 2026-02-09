# Hextra Documentation Guide

This guide describes how to use the advanced features of the Hextra theme to enhance the **Extraction Project GDD**.

## Callouts

Use callouts to highlight important information, designer notes, or technical warnings.

```markdown
{{</* callout type="info" */>}}
**Designer Note:** The recoil pattern should feel heavy but predictable.
{{</* /callout */>}}

{{</* callout type="warning" */>}}
**Technical Warning:** Reducing the tick rate below 30Hz will cause noticeable desync in physics.
{{</* /callout */>}}

{{</* callout type="error" */>}}
**Critical:** Anti-cheat must be initialized before any gameplay logic starts.
{{</* /callout */>}}
```

## Mermaid Diagrams

You can embed diagrams directly in Markdown. Perfect for logic flows and state machines. Hextra renders these automatically from code blocks with the `mermaid` language.

```markdown
```mermaid
graph TD;
    Start[Start Raid] --> Loot[Search for Items];
    Loot --> Combat{Enemy Spotted?};
    Combat -- Yes --> Fight[Engage/Retreat];
    Combat -- No --> Extraction[Go to Extract];
    Fight --> Extraction;
    Extraction --> Done[Return to Hideout];
```
```

## Tabs

Use tabs to compare different versions, platform settings, or weapon classes.

```markdown
{{</* tabs */>}}
  {{</* tab name="M4A1" */>}}**M4A1**: High fire rate, low damage per hit.{{</* /tab */>}}
  {{</* tab name="AK-74" */>}}**AK-74**: Medium fire rate, high penetration.{{</* /tab */>}}
  {{</* tab name="MP5" */>}}**MP5**: Very high fire rate, low penetration, close range.{{</* /tab */>}}
{{</* /tabs */>}}
```

## File Tree

Use the file tree to explain the project structure of the Unreal Engine project.

```markdown
{{</* filetree */>}}
  {{</* folder name="Content" */>}}
    {{</* folder name="Blueprints" */>}}
      {{</* file name="BP_PlayerCharacter.uasset" */>}}
      {{</* file name="BP_WeaponBase.uasset" */>}}
    {{</* /folder */>}}
    {{</* folder name="Maps" */>}}
      {{</* file name="TutorialRaid.umap" */>}}
    {{</* /folder */>}}
  {{</* /folder */>}}
{{</* /filetree */>}}
```

## Steps

Great for tutorial walkthroughs or installation steps.

```markdown
{{</* steps */>}}

### Step 1: Initialize Project
Clone the repository and run `git submodule update`.

### Step 2: Build Assets
Run the build script to compile shaders.

### Step 3: Launch
Open the project in Unreal Editor 5.x.

{{</* /steps */>}}
```

## Cards

Useful for landing pages or linking to major sections.

```markdown
{{</* cards */>}}
  {{</* card link="/GDD_Design/" title="Design GDD" icon="pencil" */>}}
  {{</* card link="/GDD_Technical/" title="Technical GDD" icon="code" */>}}
{{</* /cards */>}}
```
