from pathlib import Path
import json

p=Path('App.tsx'); s=p.read_text()

def rep(old,new):
    global s
    if old not in s: raise SystemExit('anchor missing: '+old[:40])
    s=s.replace(old,new,1)

rep('''const COLORS = {
  background: "#F8F2E8",
  surface: "#FFFDF8",
  ink: "#173F3B",
  muted: "#6E7973",
  primary: "#1E7A75",
  primaryDeep: "#0F5F5B",
  lavender: "#DDEBE6",
  lavenderSoft: "#F3F0E7",
  peach: "#EACDB8",
  blush: "#F6E4DA",
  sky: "#E7EFEA",
  border: "#E5D9C9",''','''const COLORS = {
  background: "#F4EBDD",
  surface: "#FFFDF8",
  ink: "#163F3A",
  muted: "#70736B",
  primary: "#2F817C",
  primaryDeep: "#0F5F5B",
  lavender: "#DDE8E1",
  lavenderSoft: "#F7F1E7",
  peach: "#E8CDB9",
  blush: "#F3DDD0",
  sky: "#E8EFEA",
  gold: "#D4A84A",
  sage: "#94A79A",
  border: "#E2D6C5",''')
rep('''function AppButton({
''','''function Soft3DIcon({ icon, size = 44, tint = COLORS.primary, glyphColor = COLORS.primaryDeep }: { icon: IconName; size?: number; tint?: string; glyphColor?: string }) {
  const radius = Math.round(size * 0.31);
  return (
    <View style={[styles.soft3dWrap, { width: size + 5, height: size + 7 }]}>
      <View style={[styles.soft3dShadow, { width: size, height: size, borderRadius: radius, backgroundColor: tint }]} />
      <View style={[styles.soft3dBack, { width: size, height: size, borderRadius: radius, backgroundColor: tint }]} />
      <View style={[styles.soft3dFace, { width: size, height: size, borderRadius: radius, backgroundColor: COLORS.surface, borderColor: tint }]}>
        <View style={[styles.soft3dInset, { width: size * 0.76, height: size * 0.76, borderRadius: radius * 0.78, backgroundColor: tint }]}>
          <MaterialIcons name={icon} size={size * 0.43} color={glyphColor} />
        </View>
      </View>
    </View>
  );
}

function AppButton({
''')
rep('''function Metric({ icon, label, value, tint }: { icon: IconName; label: string; value: string | number; tint: string }) {
  return (
    <View style={styles.metricCard}>
      <View style={[styles.metricIcon, { backgroundColor: tint }]}>
        <MaterialIcons name={icon} size={20} color={COLORS.primaryDeep} />
      </View>
      <Text style={styles.metricValue}>{value}</Text>
      <Text style={styles.metricLabel}>{label}</Text>
    </View>
  );
}
''','''function Metric({ icon, label, value, tint }: { icon: IconName; label: string; value: string | number; tint: string }) {
  return (
    <View style={styles.metricCard}>
      <Soft3DIcon icon={icon} size={42} tint={tint} />
      <Text style={styles.metricValue}>{value}</Text>
      <Text style={styles.metricLabel}>{label}</Text>
    </View>
  );
}
''')
rep('<MaterialIcons name={icon} size={20} color={tone === "danger" ? COLORS.danger : COLORS.primaryDeep} />','<Soft3DIcon icon={icon} size={30} tint={tone === "danger" ? COLORS.dangerSoft : COLORS.lavenderSoft} glyphColor={tone === "danger" ? COLORS.danger : COLORS.primaryDeep} />')
rep('''      <View style={styles.brandRow}>
        <View style={styles.brandMark}><Image source={require("./assets/nanelsh-logo.png")} style={styles.brandLogo} resizeMode="contain" /></View>
        <View>
          <Text style={styles.brandName}>NANELSH Academy</Text>
          <Text style={styles.brandCaption}>نظام إدارة الأكاديمية</Text>
        </View>
      </View>''','''      <View style={styles.brandRow}>
        <View style={styles.brandMarkPremium}>
          <Image source={require("./assets/nanelsh-logo.png")} style={styles.brandLogoPremium} resizeMode="contain" />
        </View>
        <View style={styles.brandTextBlock}>
          <Text style={styles.brandName}>NANELSH Academy</Text>
          <Text style={styles.brandCaption}>نظام إدارة الأكاديمية</Text>
        </View>
        <MaterialIcons name="eco" size={20} color={COLORS.sage} />
      </View>''')
rep('''          <View style={styles.heroCard}>
            <View style={styles.heroGlowOne} />
            <View style={styles.heroGlowTwo} />
            <Text style={styles.heroEyebrow}>مركز التحكم اليومي</Text>
            <Text style={styles.heroTitle}>مرحبًا بكِ في يومك التعليمي</Text>
            <Text style={styles.heroBody}>{formatDate(today)}</Text>
            <View style={styles.heroActions}>
              <AppButton title="إضافة حصة" icon="add-circle-outline" onPress={() => onOpen("session")} tone="soft" compact />
              <AppButton title="إضافة طالبة" icon="person-add-alt-1" onPress={() => onOpen("student")} tone="outline" compact />
            </View>
          </View>''','''          <View style={styles.heroCard}>
            <View style={styles.heroGlowOne} />
            <View style={styles.heroGlowTwo} />
            <View style={styles.heroLeafOne}><MaterialIcons name="eco" size={56} color="rgba(244,235,221,0.34)" /></View>
            <View style={styles.heroLeafTwo}><MaterialIcons name="local-florist" size={42} color="rgba(232,205,185,0.28)" /></View>
            <View style={styles.heroBrandLine}><MaterialIcons name="science" size={19} color={COLORS.gold} /><Text style={styles.heroEyebrow}>NANELSH ACADEMY OS · مركز التحكم اليومي</Text></View>
            <Text style={styles.heroTitle}>مرحبًا بكِ في عالمك الأكاديمي</Text>
            <Text style={styles.heroBody}>{formatDate(today)}  ·  تعليم جميل، إدارة هادئة، يومك تحت السيطرة</Text>
            <View style={styles.heroActions}>
              <AppButton title="إضافة حصة" icon="add-circle-outline" onPress={() => onOpen("session")} tone="soft" compact />
              <AppButton title="إضافة طالبة" icon="person-add-alt-1" onPress={() => onOpen("student")} tone="outline" compact />
            </View>
          </View>''')
rep('<View style={[styles.tabIcon, selected && styles.tabIconSelected]}><MaterialIcons name={tab.icon} size={22} color={selected ? COLORS.primaryDeep : COLORS.muted} /></View>','<View style={[styles.tabIcon, selected && styles.tabIconSelected]}><Soft3DIcon icon={tab.icon} size={30} tint={selected ? COLORS.peach : COLORS.lavenderSoft} glyphColor={selected ? COLORS.primaryDeep : COLORS.muted} /></View>')
for a,b in {
'  appHeader: { height: 76, paddingHorizontal: 18,':'  appHeader: { height: 82, paddingHorizontal: 18,',
'  brandLogo: { width: 34, height: 34, borderRadius: 10 }, brandMark:':'  brandLogo: { width: 34, height: 34, borderRadius: 10 }, brandLogoPremium: { width: 52, height: 52, borderRadius: 16 }, brandMarkPremium: { width: 58, height: 58, borderRadius: 20, backgroundColor: "#F7F0E5", alignItems: "center", justifyContent: "center", borderWidth: 1, borderColor: COLORS.border, shadowColor: "#7E7568", shadowOpacity: 0.14, shadowOffset: { width: 0, height: 5 }, shadowRadius: 10, elevation: 4 }, brandTextBlock: { gap: 1 }, brandMark:',
'  iconButton: { width: 38, height: 38, alignItems: "center", justifyContent: "center", backgroundColor: COLORS.lavenderSoft, borderRadius: 13 },':'  iconButton: { width: 42, height: 42, alignItems: "center", justifyContent: "center", backgroundColor: COLORS.surface, borderRadius: 15, borderWidth: 1, borderColor: COLORS.border, shadowColor: "#7A7165", shadowOpacity: 0.10, shadowOffset: { width: 0, height: 4 }, shadowRadius: 8, elevation: 3 },',
'  heroCard: { overflow: "hidden", borderRadius: 26, padding: 22, backgroundColor: COLORS.primaryDeep, minHeight: 194, justifyContent: "center", marginBottom: 4 },':'  heroCard: { overflow: "hidden", borderRadius: 30, padding: 22, backgroundColor: COLORS.primaryDeep, minHeight: 208, justifyContent: "center", marginBottom: 4, borderWidth: 1, borderColor: "rgba(255,255,255,0.12)", shadowColor: COLORS.primaryDeep, shadowOpacity: 0.20, shadowOffset: { width: 0, height: 9 }, shadowRadius: 18, elevation: 7 },',
'  heroGlowTwo: { position: "absolute", width: 160, height: 160, borderRadius: 80, backgroundColor: "rgba(247,223,201,0.18)", right: -55, bottom: -75 },':'  heroGlowTwo: { position: "absolute", width: 180, height: 180, borderRadius: 90, backgroundColor: "rgba(247,223,201,0.18)", right: -70, bottom: -85 },\n  heroLeafOne: { position: "absolute", left: 18, top: 18, transform: [{ rotate: "-18deg" }] }, heroLeafTwo: { position: "absolute", right: 24, bottom: 18, transform: [{ rotate: "14deg" }] },\n  heroBrandLine: { flexDirection: "row-reverse", alignItems: "center", gap: 7, alignSelf: "flex-end" },',
'  heroTitle: { color: "#FFFDF8", fontSize: 25, lineHeight: 34, fontWeight: "800", marginTop: 6, textAlign: "right", writingDirection: "rtl" },':'  heroTitle: { color: "#FFFDF8", fontSize: 26, lineHeight: 35, fontWeight: "900", marginTop: 8, textAlign: "right", writingDirection: "rtl" },',
'  metricCard: { width: "48.5%", backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, borderRadius: 20, padding: 14 },':'  metricCard: { width: "48.5%", backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, borderRadius: 24, padding: 14, shadowColor: "#7A7165", shadowOpacity: 0.08, shadowOffset: { width: 0, height: 5 }, shadowRadius: 10, elevation: 2 },',
'tabIcon: { width: 37, height: 29, borderRadius: 11, alignItems: "center", justifyContent: "center" }':'tabIcon: { width: 44, height: 39, borderRadius: 13, alignItems: "center", justifyContent: "center" }',
}.items(): rep(a,b)
rep('  tabBar: { flexDirection: "row-reverse", minHeight: 71, paddingHorizontal: 4, paddingTop: 7, paddingBottom: 8, backgroundColor: "#FFFDF8", borderTopWidth: 1, borderTopColor: COLORS.border, justifyContent: "space-around" },','  soft3dWrap: { position: "relative", alignItems: "center", justifyContent: "center" }, soft3dShadow: { position: "absolute", left: 3, top: 6, opacity: 0.20, transform: [{ scaleX: 0.96 }] }, soft3dBack: { position: "absolute", left: 0, top: 3, opacity: 0.55 }, soft3dFace: { alignItems: "center", justifyContent: "center", borderWidth: 1, shadowColor: "#675F55", shadowOpacity: 0.13, shadowOffset: { width: 0, height: 4 }, shadowRadius: 7, elevation: 4 }, soft3dInset: { alignItems: "center", justifyContent: "center", shadowColor: "#fff", shadowOpacity: 0.45, shadowOffset: { width: -1, height: -2 }, shadowRadius: 3, elevation: 1 },\n  tabBar: { flexDirection: "row-reverse", minHeight: 78, paddingHorizontal: 4, paddingTop: 7, paddingBottom: 8, backgroundColor: "#FBF6ED", borderTopWidth: 1, borderTopColor: COLORS.border, justifyContent: "space-around", shadowColor: "#6B6257", shadowOpacity: 0.08, shadowOffset: { width: 0, height: -4 }, shadowRadius: 10, elevation: 8 },')
p.write_text(s)
a=Path('app.json'); d=json.loads(a.read_text()); d['expo']['version']='2.3.0'; d['expo']['android']['versionCode']=7; d['expo']['splash']['backgroundColor']='#F4EBDD'; d['expo']['android']['adaptiveIcon']['backgroundColor']='#F4EBDD'; [plugin[1].__setitem__('color','#2F817C') for plugin in d['expo']['plugins'] if isinstance(plugin,list) and plugin and plugin[0]=='expo-notifications']; a.write_text(json.dumps(d,ensure_ascii=False,indent=2)+'\n')
print('NANELSH final visual skin applied')
