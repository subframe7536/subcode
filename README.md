> [!note]
> ### When will V7 become stable?
> It is almost stable now.
>
> As a side project during my weekends, I will release a new beta version to fix the bugs reported or encountered in my daily coding within 1-2 weeks, and do some work on the new website and build tools.
>
> If everything goes well, the stable version will be released later this year.

# Maple Font (WIP)

Open source monospace & nerd font with round corner and ligatures.

Based on `JetBrains Mono` and **much "Opinioned"**

![](https://github.com/subframe7536/maple-font/assets/78338239/19383849-6be1-4cfc-9b34-7b33fc047ecf)

- Generated by [CodeImg](https://github.com/subframe7536/vscode-codeimg)
- Theme: [Maple](https://github.com/subframe7536/vscode-theme-maple)

## Features

- Round corner
- New shape of `@ $ % & Q a` and cursive italic `f i j k l x y`
- Large amount of ligatures, see in [`features/`](./source/features/README.md)

## Build

Clone the repo and run on your local machine. Make sure you have `python3` and `pip` installed

```shell
git clone https://github.com/subframe7536/maple-font --depth 1 -b variable
pip install foundrytools-cli
python build.py
```

- For `Ubuntu` or `Debian`, maybe `python-is-python3` is needed as well

If you have trouble installing the dependencies, just create a new Github codespace on `variable` branch and run the commands there

### Customize

You can change build config in `config.json`

- There is `--normal` option in `build.py` for common config, just like `JetBrains Mono` (with slashed zero)
- For custom `font-patcher` args, `font-forge` (and maybe `python3-fontforge` as well) is needed

#### Font Feature Freeze Options

- `enable`: Move ligature rules to `calt`, which will enable the features without setting up `cvXX` / `ssXX` / `zero` in font features config, just as default ligatures
- `disable`: Remove the features in `cvXX` / `ssXX` / `zero`, which will no longer effect, even if you enable it manually
- `ignore`: Do nothing

### Chinese version

1. Download CN base font at [Gitee release](https://gitee.com/subframe7536/Maple/releases/tag/v7.0-beta23)
2. Put them into `./source/cn`
3. Run `build.py` and **BE PATIENT**, instantiation will take about 40-50 minutes

#### Notice

If you have trouble downloading `Font Patcher`, setup `nerd_font.github_mirror` in `config.json` or setup `$GITHUB` to your environment variable.

### Release Build

```sh
python build.py --release
```

## Credit

- [JetBrains Mono](https://github.com/JetBrains/JetBrainsMono)
- [Roboto Mono](https://github.com/googlefonts/RobotoMono)
- [Fira Code](https://github.com/tonsky/FiraCode)
- [Victor Mono](https://github.com/rubjo/victor-mono)
- [Commit Mono](https://github.com/eigilnikolajsen/commit-mono)
- [Code Sample](https://github.com/TheRenegadeCoder/sample-programs-website)
- [Nerd Font](https://github.com/ryanoasis/nerd-fonts)
- [Font Freeze](https://github.com/MuTsunTsai/fontfreeze/)
- [Font Viewer](https://tophix.com/font-tools/font-viewer)
- [Monolisa](https://www.monolisa.dev/) for landing page
- [Recursive](https://www.recursive.design/)

## License

SIL Open Font License 1.1
