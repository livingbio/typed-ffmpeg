//! Parse FFmpeg full help output (`ffmpeg -h full`).

use anyhow::Result;

use super::utils::{
    parse_av_option, parse_general_option, parse_section_tree, run_ffmpeg_command,
};
use crate::schema::parse_help::HelpOption;

/// Parse FFmpeg help text into structured options.
fn parse(help_text: &str) -> Result<Vec<HelpOption>> {
    let tree = parse_section_tree(help_text);
    let mut output = Vec::new();

    for section in tree.keys() {
        if section.contains("options") {
            output.extend(
                parse_general_option(section, &tree)?
                    .into_iter()
                    .map(Into::into),
            );
        } else if section.contains("AVOptions") {
            output.extend(
                parse_av_option(section, &tree)?
                    .into_iter()
                    .map(|av| HelpOption {
                        section: av.section,
                        name: av.name,
                        option_type: av.option_type,
                        flags: av.flags,
                        help: av.help,
                        argname: av.argname,
                    }),
            );
        }
    }

    Ok(output)
}

/// Extract all options from FFmpeg's full help output.
pub fn extract(ffmpeg_binary: &str) -> Result<Vec<HelpOption>> {
    let text = run_ffmpeg_command(&["-h", "full"], ffmpeg_binary)?;
    parse(&text)
}
