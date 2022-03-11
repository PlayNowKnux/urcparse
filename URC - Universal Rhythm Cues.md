# URC - Universal Rhythm Cues

Do you want to put a sound on a beat, but you just don't have precise enough software?
Never fear, URC is here!
The URC file format is meant to easily map timed events (like sound effects or cues in rhythm games) to music.

This format was built to work with many types of 
applications, and users can build their own programs to handle 
the files.

## Structure

The file is structured in two parts: the metadata block, and the cue block. 
These blocks are separated by a `start` command.
The metadata block includes timing commands and, of course, metadata commands.
The cue block includes the cue commands, like `r` and `m`.
Here is a rough outline of what a URC file should look like:

```
meta
off, soff

start

r, m, apply
```

## Metadata block

### `meta`

Adds metadata to the file, can be used to change compilation settings.

Syntax:

`meta <Key> <Value>`

* `Key` is the key of the metadata. It cannot have spaces.
* `Value` is what goes into `Key`. It can have spaces.


Usage:

```URC
// BaseFile defines the file being modified
meta BaseFile amenbeat.mp3

// ExportFile defines where the modified file is being exported
meta ExportFile Amen Beat with EXPLOSIONS!!!.mp3
```

---

### `off`

**`r` WILL NOT WORK WITHOUT THIS COMMAND**

Defines where some measures begin (like the first measure and where tempo changes are).
Always ends with a `#`.

Syntax:
```
off <type> <start>:
    // offset commands like bpm and ts
#
```

* `type` can either be `fb` (`start` is a beat) or `st` (`start` is the start of the song
  \[not implemented as of March 9, 2022\]).
* `start` is a time in milliseconds after the song has started.

```URC
off fb 3800:
	// 4/4 time signature is assumed
	bpm 200
#
off fb 148352:
	ts 3/4
	bpm 150
#
```
---
### `bpm`

Sets the bpm for an `off` command. Without this command in an `off` block, the bpm will be 120.

Syntax:

`bpm <tempo>`

* `tempo` is the tempo of the offset block.

Usage:

```URC
off fb 148352:
	ts 3/4
	
	// Set the tempo to 150 beats per minute
	bpm 150
#
```
---
### `ts`

Sets the time for an `off` command. Without this command in an `off` block, the time signature will be 4/4.

Syntax:

`ts <timeSignature>`

* `timeSignature` is the time signature of the offset block. It is written like `4/4`, `3/4`, `6/8`, etc.

Usage:

```URC
off fb 148352:
    // Set the time signature to 3/4
    ts 3/4
    bpm 150
#
```
---