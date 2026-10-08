from pathlib import Path
p=Path("App.tsx")
s=p.read_text()

# Personal palette
s=s.replace('  successSoft: "#E7F0EA",\n};','  successSoft: "#E7F0EA",\n  terracotta: "#B86F5B",\n  terracottaSoft: "#F3E3DC",\n};')

# Brand voice
s=s.replace("NANELSH · SIGNATURE ACADEMY OS","NANELSH · MY ACADEMY")
s=s.replace("NANELSH · FLAGSHIP OS","NANELSH · MY ACADEMY")
s=s.replace("هوية ذكية لإدارة أكاديميتك بكل أناقة","علوم · طلاب · حصص · أكاديمية")

# Make the session action the visual anchor
s=s.replace('{ label: "حصة", icon: "add-circle-outline" as IconName, action: () => onOpen("session") },','{ label: "حصة", icon: "add-circle-outline" as IconName, action: () => onOpen("session"), primary: true },')
s=s.replace('{ label: "طالبة", icon: "person-add-alt-1" as IconName, action: () => onOpen("student") },','{ label: "طالبة", icon: "person-add-alt-1" as IconName, action: () => onOpen("student"), primary: false },')
s=s.replace('{ label: "دفعة", icon: "payments" as IconName, action: () => onOpen("finance") },','{ label: "دفعة", icon: "payments" as IconName, action: () => onOpen("finance"), primary: false },')
s=s.replace('{ label: "مجموعة", icon: "groups" as IconName, action: () => onOpen("group") },','{ label: "مجموعة", icon: "groups" as IconName, action: () => onOpen("group"), primary: false },')

# Personal signature + subtle science motif
anchor='<Text style={styles.commandDate}>{formatDate(today)}</Text>'
insert='<Text style={styles.commandDate}>{formatDate(today)}</Text>\n            <View style={styles.commandSignatureRow}><Text style={styles.commandSignature}>تعليم جميل · إدارة هادئة · يومك تحت السيطرة</Text><View style={styles.commandScientificMark}><View style={styles.scientificDot} /><View style={styles.scientificDotSmall} /><View style={styles.scientificDot} /></View></View>'
s=s.replace(anchor,insert,1)

# Quick action treatment
old='<Pressable key={item.label} accessibilityRole="button" accessibilityLabel={`إضافة ${item.label}`} onPress={() => { haptic(); item.action(); }} style={({ pressed }) => [styles.quickAction, pressed && { opacity: 0.72, transform: [{ scale: 0.98 }] }]}><View style={styles.quickActionIcon}><MaterialIcons name={item.icon} size={21} color={COLORS.primaryDeep} /></View><Text style={styles.quickActionText}>إضافة {item.label}</Text></Pressable>'
new='<Pressable key={item.label} accessibilityRole="button" accessibilityLabel={`إضافة ${item.label}`} onPress={() => { haptic(); item.action(); }} style={({ pressed }) => [styles.quickAction, item.primary && styles.quickActionPrimary, pressed && { opacity: 0.72, transform: [{ scale: 0.97 }] }]}><View style={[styles.quickActionIcon, item.primary && styles.quickActionIconPrimary]}><MaterialIcons name={item.icon} size={21} color={item.primary ? COLORS.surface : COLORS.primaryDeep} /></View><Text style={[styles.quickActionText, item.primary && styles.quickActionTextPrimary]}>إضافة {item.label}</Text></Pressable>'
s=s.replace(old,new,1)
# Support the already-polished source variant as well.
s=s.replace('style={({ pressed }) => [styles.quickAction, pressed && { opacity: 0.72, transform: [{ scale: 0.97 }] }]}>', 'style={({ pressed }) => [styles.quickAction, item.primary && styles.quickActionPrimary, pressed && { opacity: 0.72, transform: [{ scale: 0.97 }] }]}>', 1)

# Editorial language
s=s.replace('FLAGSHIP PULSE</Text>','NANELSH TODAY</Text>',1)
s=s.replace('صورة سريعة عن الأكاديمية</Text>','لمحة صغيرة عن يومك</Text>',1)

# End session: calm positive check action
s=s.replace('onComplete ? <AppButton title="إنهاء الحصة" icon="check-circle-outline" onPress={onComplete} tone={session.status === "scheduled" ? "outline" : "primary"} compact /> : null','onComplete ? <AppButton title="إنهاء الحصة" icon="check-circle" onPress={onComplete} tone="soft" compact /> : null',1)

# Header
s=s.replace('appHeader: { height: 82, paddingHorizontal: 16, flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between", backgroundColor: "#FBF8F1", borderBottomWidth: 1, borderBottomColor: COLORS.border, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.035, shadowOffset: { width: 0, height: 3 }, shadowRadius: 10, elevation: 2 },','appHeader: { height: 88, paddingHorizontal: 16, flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between", backgroundColor: COLORS.background, borderBottomWidth: 1, borderBottomColor: "rgba(197,164,109,0.22)" },')
s=s.replace('brandMarkFrame: { width: 48, height: 48, borderRadius: 17, overflow: "hidden", backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.champagneSoft, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.10, shadowOffset: { width: 0, height: 5 }, shadowRadius: 10, elevation: 3 },','brandMarkFrame: { width: 46, height: 46, borderRadius: 15, overflow: "hidden", backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.champagneSoft },')
s=s.replace('brandEyebrow: { color: COLORS.champagne, fontSize: 8,','brandEyebrow: { color: COLORS.terracotta, fontSize: 8,')
s=s.replace('brandName: { color: COLORS.ink, fontSize: 16,','brandName: { color: COLORS.primaryDeep, fontSize: 17,')

# Main hero becomes warm/editorial instead of SaaS-dark
s=s.replace('commandCenter: { overflow: "hidden", borderRadius: 30, padding: 20, backgroundColor: COLORS.primaryDeep, minHeight: 198, borderWidth: 1, borderColor: "rgba(197,164,109,0.52)", shadowColor: COLORS.primaryDeep, shadowOpacity: 0.18, shadowOffset: { width: 0, height: 12 }, shadowRadius: 24, elevation: 6 },','commandCenter: { overflow: "hidden", borderRadius: 30, padding: 20, backgroundColor: COLORS.surface, minHeight: 218, borderWidth: 1, borderColor: "rgba(184,111,91,0.28)", shadowColor: COLORS.primaryDeep, shadowOpacity: 0.07, shadowOffset: { width: 0, height: 8 }, shadowRadius: 20, elevation: 3 },')
s=s.replace('commandOrbOne: { position: "absolute", width: 190, height: 190, borderRadius: 95, backgroundColor: "rgba(197,164,109,0.17)", top: -122, left: -52 },','commandOrbOne: { position: "absolute", width: 190, height: 190, borderRadius: 95, backgroundColor: "rgba(184,111,91,0.10)", top: -122, left: -52 },')
s=s.replace('commandOrbTwo: { position: "absolute", width: 145, height: 145, borderRadius: 73, backgroundColor: "rgba(220,233,228,0.12)", right: -60, bottom: -72 },','commandOrbTwo: { position: "absolute", width: 145, height: 145, borderRadius: 73, backgroundColor: "rgba(27,116,107,0.08)", right: -60, bottom: -72 },')
s=s.replace('commandEyebrow: { color: COLORS.champagne,','commandEyebrow: { color: COLORS.terracotta,')
s=s.replace('commandLive: { flexDirection: "row-reverse", alignItems: "center", gap: 6, paddingHorizontal: 9, minHeight: 27, borderRadius: 14, backgroundColor: "rgba(255,255,255,0.10)", borderWidth: 1, borderColor: "rgba(255,255,255,0.12)" },','commandLive: { flexDirection: "row-reverse", alignItems: "center", gap: 6, paddingHorizontal: 9, minHeight: 27, borderRadius: 14, backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: COLORS.border },')
s=s.replace('commandLiveText: { color: "#E7F0EA",','commandLiveText: { color: COLORS.primaryDeep,')
s=s.replace('commandGreeting: { color: "#FFFFFF",','commandGreeting: { color: COLORS.primaryDeep,')
s=s.replace('commandDate: { color: "#DCE9E4",','commandDate: { color: COLORS.muted,')
s=s.replace('commandSummaryRow: { flexDirection: "row-reverse", alignItems: "center", marginTop: 19, paddingTop: 14, borderTopWidth: 1, borderTopColor: "rgba(255,255,255,0.12)" },','commandSummaryRow: { flexDirection: "row-reverse", alignItems: "center", marginTop: 16, paddingTop: 14, borderTopWidth: 1, borderTopColor: COLORS.border },')
s=s.replace('commandSummaryValue: { color: "#FFFFFF",','commandSummaryValue: { color: COLORS.primaryDeep,')
s=s.replace('commandSummaryLabel: { color: "#BFD0C9",','commandSummaryLabel: { color: COLORS.muted,')
s=s.replace('commandSummaryDivider: { width: 1, height: 30, backgroundColor: "rgba(255,255,255,0.12)" },','commandSummaryDivider: { width: 1, height: 30, backgroundColor: COLORS.border },')

# Next session feels like a personal planner card
s=s.replace('nextSessionCard: { minHeight: 102, flexDirection: "row-reverse", alignItems: "center", gap: 11, overflow: "hidden", backgroundColor: COLORS.surface, borderRadius: 22, borderWidth: 1, borderColor: "rgba(197,164,109,0.36)", padding: 13, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.06, shadowOffset: { width: 0, height: 5 }, shadowRadius: 14, elevation: 2 },','nextSessionCard: { minHeight: 108, flexDirection: "row-reverse", alignItems: "center", gap: 11, overflow: "hidden", backgroundColor: COLORS.sandSoft, borderRadius: 24, borderWidth: 1, borderColor: "rgba(184,111,91,0.22)", padding: 14 },')
s=s.replace('nextSessionAccent: { position: "absolute", right: 0, top: 0, bottom: 0, width: 4, backgroundColor: COLORS.champagne },','nextSessionAccent: { position: "absolute", right: 0, top: 0, bottom: 0, width: 5, backgroundColor: COLORS.terracotta },')
s=s.replace('nextSessionEyebrow: { color: COLORS.champagne,','nextSessionEyebrow: { color: COLORS.terracotta,')

# Quick actions lose the rigid dashboard-card feel
s=s.replace('quickActionsCard: { backgroundColor: "rgba(255,254,251,0.88)", borderRadius: 22, borderWidth: 1, borderColor: COLORS.border, padding: 13, shadowColor: COLORS.primaryDeep, shadowOpacity: 0.035, shadowOffset: { width: 0, height: 4 }, shadowRadius: 10, elevation: 1 },','quickActionsCard: { backgroundColor: "transparent", borderRadius: 0, paddingVertical: 2, paddingHorizontal: 0 },')
s=s.replace('quickAction: { flex: 1, minHeight: 68, alignItems: "center", justifyContent: "center", borderRadius: 16, backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: "#E1EAE4", gap: 5 },','quickAction: { flex: 1, minHeight: 66, alignItems: "center", justifyContent: "center", borderRadius: 19, backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, gap: 5 }, quickActionPrimary: { backgroundColor: COLORS.primaryDeep, borderColor: COLORS.primaryDeep },')
s=s.replace('quickActionIcon: { width: 31, height: 31, borderRadius: 10,','quickActionIcon: { width: 32, height: 32, borderRadius: 11,')
s=s.replace('quickActionText: { color: COLORS.primaryDeep, fontSize: 9, fontWeight: "800",','quickActionText: { color: COLORS.primaryDeep, fontSize: 9, fontWeight: "900",')
# Inject action-specific styles after quickActionText
s=s.replace('quickActionText: { color: COLORS.primaryDeep, fontSize: 9, fontWeight: "900", textAlign: "center", writingDirection: "rtl" },','quickActionText: { color: COLORS.primaryDeep, fontSize: 9, fontWeight: "900", textAlign: "center", writingDirection: "rtl" }, quickActionTextPrimary: { color: COLORS.surface }, quickActionIconPrimary: { backgroundColor: "rgba(255,255,255,0.14)", borderColor: "rgba(255,255,255,0.20)" },')

# Pulse becomes an editorial section, not another container
s=s.replace('flagshipPulse: { backgroundColor: COLORS.surface, borderRadius: 23, borderWidth: 1, borderColor: COLORS.border, padding: 14, marginBottom: 2,','flagshipPulse: { backgroundColor: "transparent", borderRadius: 0, borderWidth: 0, borderColor: "transparent", padding: 0, marginBottom: 4,')
s=s.replace('flagshipPulseBadge: { flexDirection: "row-reverse", alignItems: "center", gap: 5, paddingHorizontal: 8, paddingVertical: 5, borderRadius: 10, backgroundColor: COLORS.primaryDeep },','flagshipPulseBadge: { flexDirection: "row-reverse", alignItems: "center", gap: 5, paddingHorizontal: 9, paddingVertical: 5, borderRadius: 12, backgroundColor: COLORS.terracottaSoft },')
s=s.replace('flagshipPulseBadgeText: { color: COLORS.champagne,','flagshipPulseBadgeText: { color: COLORS.terracotta,')
s=s.replace('flagshipPulseMetric: { flex: 1, alignItems: "flex-end", padding: 9, borderRadius: 16, backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: "#E4EBE6" },','flagshipPulseMetric: { flex: 1, alignItems: "flex-end", padding: 11, borderRadius: 18, backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border },')

# Calm button language
s=s.replace('button: { minHeight: 47, borderRadius: 16,','button: { minHeight: 47, borderRadius: 17,')
# Signature styles
sig='commandSignatureRow: { flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between", marginTop: 9 }, commandSignature: { color: COLORS.terracotta, fontSize: 9, fontWeight: "800", textAlign: "right", writingDirection: "rtl" }, commandScientificMark: { width: 44, height: 20, flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between", paddingHorizontal: 4 }, scientificDot: { width: 7, height: 7, borderRadius: 4, backgroundColor: COLORS.champagne }, scientificDotSmall: { width: 4, height: 4, borderRadius: 2, backgroundColor: COLORS.primary },'
s=s.replace('commandDate: { color: COLORS.muted, fontSize: 12, marginTop: 4, textAlign: "right", writingDirection: "rtl" },','commandDate: { color: COLORS.muted, fontSize: 12, marginTop: 4, textAlign: "right", writingDirection: "rtl" }, '+sig)
p.write_text(s)
