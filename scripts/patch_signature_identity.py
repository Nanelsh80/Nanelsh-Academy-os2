from pathlib import Path
import re

app = Path("App.tsx")
s = app.read_text()

# NANELSH SIGNATURE — visual identity reset.
# This pass intentionally changes presentation only; database and business logic stay untouched.

replacements = {
    "NANELSH · FLAGSHIP OS": "NANELSH · MY ACADEMY",
    "FLAGSHIP PULSE": "NANELSH PULSE",
    "NEXT SESSION": "الحصة القادمة",
    "هوية ذكية لإدارة أكاديميتك بكل أناقة": "مساحتك اليومية لإدارة طلابك وحصصك بكل هدوء",
}

for old, new in replacements.items():
    s = s.replace(old, new)

# Warm, editorial NANELSH palette.
palette = {
    "#F6F3EC": "#F7F3EA",
    "#153C3A": "#173F3A",
    "#C5A46D": "#B99557",
    "#DCE9E4": "#E2ECE7",
    "#252D32": "#24302E",
    "#FFFFFF": "#FFFDF8",
    "#1CA7A6": "#2C8178",
}
for old, new in palette.items():
    s = s.replace(old, new)

def replace_style(name, body):
    global s
    pattern = rf"(?m)^\s*{re.escape(name)}:\s*\{{[^\n]*\}},"
    replacement = f"  {name}: {{ {body} }},"
    s, count = re.subn(pattern, replacement, s, count=1)
    return count

# Editorial, softer cards. If a style is absent in this source, simply leave it unchanged.
style_overrides = {
    "heroCard": 'backgroundColor: COLORS.primaryDeep, borderRadius: 30, borderWidth: 1, borderColor: "rgba(185,149,87,0.55)", padding: 18, overflow: "hidden", shadowColor: COLORS.primaryDeep, shadowOpacity: 0.10, shadowOffset: { width: 0, height: 10 }, shadowRadius: 24, elevation: 3',
    "heroTitle": 'color: COLORS.surface, fontSize: 27, fontWeight: "900", lineHeight: 36, textAlign: "right", writingDirection: "rtl"',
    "heroGlow": 'position: "absolute", width: 190, height: 190, borderRadius: 95, backgroundColor: "rgba(185,149,87,0.10)", top: -80, left: -55',
    "nextSessionCard": 'backgroundColor: COLORS.surface, borderRadius: 24, borderWidth: 1, borderColor: COLORS.border, padding: 16, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.06, shadowOffset: { width: 0, height: 6 }, shadowRadius: 16, elevation: 2',
    "nextSessionEyebrow": 'color: COLORS.champagne, fontSize: 9, fontWeight: "900", letterSpacing: 1.1, textAlign: "right"',
    "nextSessionTitle": 'color: COLORS.ink, fontSize: 22, fontWeight: "900", textAlign: "right", writingDirection: "rtl"',
    "nextSessionMeta": 'color: COLORS.muted, fontSize: 11, textAlign: "right", writingDirection: "rtl"',
    "quickActionsCard": 'backgroundColor: "transparent", borderWidth: 0, borderRadius: 0, padding: 0',
    "quickActionsTitle": 'color: COLORS.ink, fontSize: 18, fontWeight: "900", textAlign: "right", writingDirection: "rtl", marginBottom: 8',
    "quickActionsGrid": 'flexDirection: "row-reverse", gap: 9',
    "quickAction": 'flex: 1, minHeight: 72, alignItems: "center", justifyContent: "center", borderRadius: 20, backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, gap: 6, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.035, shadowOffset: { width: 0, height: 4 }, shadowRadius: 10, elevation: 1',
    "quickActionPrimary": 'backgroundColor: COLORS.primary, borderColor: COLORS.primary, shadowOpacity: 0.10',
    "quickActionIcon": 'width: 34, height: 34, borderRadius: 12, alignItems: "center", justifyContent: "center", backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: COLORS.border',
    "quickActionIconPrimary": 'backgroundColor: "rgba(255,255,255,0.16)", borderColor: "rgba(255,255,255,0.24)"',
    "quickActionText": 'color: COLORS.primaryDeep, fontSize: 9, fontWeight: "800", textAlign: "center", writingDirection: "rtl"',
    "quickActionTextPrimary": 'color: COLORS.surface, fontWeight: "900"',
    "flagshipPulse": 'backgroundColor: COLORS.primaryDeep, borderRadius: 26, borderWidth: 1, borderColor: "rgba(185,149,87,0.38)", padding: 16, marginBottom: 14, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.08, shadowOffset: { width: 0, height: 8 }, shadowRadius: 18, elevation: 2',
    "flagshipPulseBadgeText": 'color: COLORS.champagne, fontSize: 9, fontWeight: "900", letterSpacing: 1',
    "sessionCard": 'backgroundColor: COLORS.surface, borderRadius: 24, borderWidth: 1, borderColor: COLORS.border, padding: 15, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.045, shadowOffset: { width: 0, height: 5 }, shadowRadius: 14, elevation: 1',
    "sessionActions": 'flexDirection: "row-reverse", alignItems: "center", gap: 8, marginTop: 10',
    "listContent": 'paddingHorizontal: 16, paddingTop: 14, paddingBottom: 112, gap: 14, flexGrow: 1',
}

for name, body in style_overrides.items():
    replace_style(name, body)

# New finish-session language: visual styles are available for the updated action renderer.
new_styles = '''
  signatureDivider: { height: 1, backgroundColor: COLORS.border, marginVertical: 10 },
  signatureLabel: { color: COLORS.muted, fontSize: 9, fontWeight: "800", textAlign: "right", writingDirection: "rtl" },
  signatureSectionTitle: { color: COLORS.ink, fontSize: 19, fontWeight: "900", textAlign: "right", writingDirection: "rtl" },
  finishSessionButton: { minHeight: 46, paddingHorizontal: 15, borderRadius: 15, backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: COLORS.primary, alignItems: "center", justifyContent: "center", flexDirection: "row-reverse", gap: 7 },
  finishSessionButtonText: { color: COLORS.primaryDeep, fontSize: 10, fontWeight: "900", textAlign: "center", writingDirection: "rtl" },
  finishSessionIcon: { width: 24, height: 24, borderRadius: 12, backgroundColor: COLORS.surface, alignItems: "center", justifyContent: "center" },
  finishSessionDone: { backgroundColor: COLORS.sage, borderColor: COLORS.success },
  finishSessionDoneText: { color: COLORS.success },
'''

if "finishSessionButton:" not in s:
    anchor = '  profileSummary: {'
    if anchor in s:
        s = s.replace(anchor, new_styles + "\n" + anchor, 1)

app.write_text(s)
