from pathlib import Path

app = Path('App.tsx')
s = app.read_text()

state_anchor = '  const [profileBusy, setProfileBusy] = useState(false);\n'
state_insert = '''  const [profileBusy, setProfileBusy] = useState(false);
  const [groupMemberships, setGroupMemberships] = useState<Array<{ groupId: number; groupName: string; subject: string; startDate: string }>>([]);
'''
if 'const [groupMemberships, setGroupMemberships]' not in s:
    if state_anchor not in s:
        raise SystemExit('state anchor not found')
    s = s.replace(state_anchor, state_insert, 1)

load_anchor = '''    void refreshAcademicProfile(student.id).catch(error => Alert.alert("تعذر تحميل الملف الأكاديمي", error instanceof Error ? error.message : "حاولي مرة أخرى."));
'''
load_insert = '''    void refreshAcademicProfile(student.id).catch(error => Alert.alert("تعذر تحميل الملف الأكاديمي", error instanceof Error ? error.message : "حاولي مرة أخرى."));
    void Promise.all(groups.map(async group => {
      const members = await listGroupMembers(group.id);
      return members.filter(member => member.studentId === student.id).map(member => ({ groupId: group.id, groupName: group.name, subject: group.subject || "المادة غير محددة", startDate: member.startDate }));
    })).then(rows => setGroupMemberships(rows.flat())).catch(() => setGroupMemberships([]));
'''
if 'setGroupMemberships(rows.flat())' not in s:
    if load_anchor not in s:
        raise SystemExit('load anchor not found')
    s = s.replace(load_anchor, load_insert, 1)

calc_anchor = '''  const homeworkDone = homeworkItems.filter(item => item.status === "done").length;
'''
calc_insert = '''  const homeworkDone = homeworkItems.filter(item => item.status === "done").length;
  const selectedSubjectNames = subjectOptions.filter(subject => subjectIds.includes(subject.id)).map(subject => subject.nameAr);
  const upcomingStudentSessions = student ? sessions
    .filter(session => session.studentId === student.id && session.status !== "completed" && session.sessionDate >= todayDate())
    .sort((a, b) => `${a.sessionDate}T${a.startTime}`.localeCompare(`${b.sessionDate}T${b.startTime}`))
    .slice(0, 3) : [];
  const studentProgressPercent = student?.totalSessions ? Math.min(100, Math.round((student.completedSessions / student.totalSessions) * 100)) : 0;
  const homeworkPercent = homeworkItems.length ? Math.round((homeworkDone / homeworkItems.length) * 100) : 0;
'''
if 'const upcomingStudentSessions = student ? sessions' not in s:
    if calc_anchor not in s:
        raise SystemExit('calc anchor not found')
    s = s.replace(calc_anchor, calc_insert, 1)

jsx_anchor = '''      <InputField label="الاسم" value={name} onChangeText={setName} />
'''
jsx_insert = '''      <View style={styles.studentCommandHero}>
        <View style={styles.studentCommandHeroTop}>
          <View style={[styles.studentStatusPill, { backgroundColor: active ? "rgba(168,209,191,0.16)" : "rgba(200,161,90,0.16)" }]}>
            <View style={[styles.studentStatusDot, { backgroundColor: active ? "#8FC5AB" : COLORS.champagne }]} />
            <Text style={styles.studentStatusText}>{active ? "نشطة" : "موقوفة"}</Text>
          </View>
          <View style={{ flex: 1, alignItems: "flex-end" }}>
            <Text style={styles.studentCommandEyebrow}>STUDENT COMMAND CENTER</Text>
            <Text style={styles.studentCommandName}>{student?.name}</Text>
            <Text style={styles.studentCommandMeta}>{academy || "لم يُحدد الصف"}{phone ? ` · ${phone}` : ""}</Text>
          </View>
          <View style={styles.studentCommandAvatar}><Text style={styles.studentCommandAvatarText}>{student?.name.slice(0, 1)}</Text></View>
        </View>
        <View style={styles.studentCommandDivider} />
        <View style={styles.studentCommandKpis}>
          <View style={styles.studentCommandKpi}><Text style={styles.studentCommandKpiValue}>{student?.remainingSessions ?? 0}</Text><Text style={styles.studentCommandKpiLabel}>حصة متبقية</Text></View>
          <View style={styles.studentCommandKpiDivider} />
          <View style={styles.studentCommandKpi}><Text style={styles.studentCommandKpiValue}>{attendancePercent}%</Text><Text style={styles.studentCommandKpiLabel}>الحضور</Text></View>
          <View style={styles.studentCommandKpiDivider} />
          <View style={styles.studentCommandKpi}><Text style={styles.studentCommandKpiValue}>{examPercent}%</Text><Text style={styles.studentCommandKpiLabel}>الدرجات</Text></View>
          <View style={styles.studentCommandKpiDivider} />
          <View style={styles.studentCommandKpi}><Text style={[styles.studentCommandKpiValue, { color: outstandingAmount ? "#F1C6A6" : "#B9D8C7" }]}>{formatMoney(outstandingAmount)}</Text><Text style={styles.studentCommandKpiLabel}>المستحق</Text></View>
        </View>
      </View>

      <View style={styles.studentCommandProgressCard}>
        <View style={styles.studentCommandSectionTitleRow}>
          <Text style={styles.studentCommandSectionTitle}>التقدم العام</Text>
          <Text style={styles.studentCommandSectionValue}>{studentProgressPercent}%</Text>
        </View>
        <View style={styles.studentCommandProgressTrack}><View style={[styles.studentCommandProgressFill, { width: `${studentProgressPercent}%` }]} /></View>
        <Text style={styles.studentCommandHint}>{student?.completedSessions ?? 0} حصة منجزة من أصل {student?.totalSessions ?? 0} · {selectedSubjectNames.join(" · ") || "لم تُحدد مادة بعد"}</Text>
      </View>

      <View style={styles.studentCommandSection}>
        <View style={styles.studentCommandSectionHeader}><Text style={styles.studentCommandSectionTitle}>المواد والمجموعات</Text><Text style={styles.studentCommandCount}>{groupMemberships.length} تسجيل</Text></View>
        {selectedSubjectNames.length ? <View style={styles.studentCommandChipWrap}>{selectedSubjectNames.map(subject => <View key={subject} style={styles.studentCommandChip}><Text style={styles.studentCommandChipText}>{subject}</Text></View>)}</View> : null}
        {groupMemberships.length ? groupMemberships.map(item => <View key={`${item.groupId}-${item.startDate}`} style={styles.studentCommandListRow}><View style={styles.studentCommandRowIcon}><MaterialIcons name="groups" size={18} color={COLORS.primaryDeep} /></View><View style={{ flex: 1, alignItems: "flex-end" }}><Text style={styles.studentCommandRowTitle}>{item.groupName}</Text><Text style={styles.studentCommandRowSub}>{item.subject} · منذ {item.startDate}</Text></View></View>) : <Text style={styles.inlineHint}>لا توجد تسجيلات نشطة في مجموعات حاليًا؛ يمكن أن تكون المتابعة فردية.</Text>}
      </View>

      <View style={styles.studentCommandSection}>
        <View style={styles.studentCommandSectionHeader}><Text style={styles.studentCommandSectionTitle}>الحصص القادمة</Text><Text style={styles.studentCommandCount}>{upcomingStudentSessions.length}</Text></View>
        {upcomingStudentSessions.length ? upcomingStudentSessions.map(session => <View key={session.id} style={styles.studentCommandListRow}><View style={styles.studentCommandNextBadge}><Text style={styles.studentCommandNextBadgeText}>{formatDate(session.sessionDate)}</Text><Text style={styles.studentCommandNextTime}>{session.startTime}</Text></View><View style={{ flex: 1, alignItems: "flex-end" }}><Text style={styles.studentCommandRowTitle}>{session.subject || "حصة"}</Text><Text style={styles.studentCommandRowSub}>{session.groupName || "حصة فردية"} · {session.durationMinutes} دقيقة</Text></View></View>) : <Text style={styles.inlineHint}>لا توجد حصص قادمة مسجلة لهذا الطالب.</Text>}
      </View>

      <View style={styles.studentCommandMiniGrid}>
        <View style={styles.studentCommandMiniCard}><View style={[styles.studentCommandMiniIcon, { backgroundColor: COLORS.sage }]}><MaterialIcons name="assignment-turned-in" size={18} color={COLORS.primaryDeep} /></View><Text style={styles.studentCommandMiniValue}>{homeworkDone}/{homeworkItems.length}</Text><Text style={styles.studentCommandMiniLabel}>الواجبات المكتملة</Text><Text style={styles.studentCommandMiniHint}>{homeworkPercent}%</Text></View>
        <View style={styles.studentCommandMiniCard}><View style={[styles.studentCommandMiniIcon, { backgroundColor: COLORS.champagneSoft }]}><MaterialIcons name="fact-check" size={18} color={COLORS.warning} /></View><Text style={styles.studentCommandMiniValue}>{examHistory.length}</Text><Text style={styles.studentCommandMiniLabel}>نتائج الاختبارات</Text><Text style={styles.studentCommandMiniHint}>{examEarned}/{examPossible} درجة</Text></View>
        <View style={styles.studentCommandMiniCard}><View style={[styles.studentCommandMiniIcon, { backgroundColor: COLORS.successSoft }]}><MaterialIcons name="event-available" size={18} color={COLORS.success} /></View><Text style={styles.studentCommandMiniValue}>{attendancePresent}</Text><Text style={styles.studentCommandMiniLabel}>حضور / تأخير</Text><Text style={styles.studentCommandMiniHint}>من {attendanceCounted} سجل</Text></View>
        <View style={styles.studentCommandMiniCard}><View style={[styles.studentCommandMiniIcon, { backgroundColor: outstandingAmount ? COLORS.dangerSoft : COLORS.successSoft }]}><MaterialIcons name="account-balance-wallet" size={18} color={outstandingAmount ? COLORS.danger : COLORS.success} /></View><Text style={styles.studentCommandMiniValue}>{formatMoney(paidAmount)}</Text><Text style={styles.studentCommandMiniLabel}>صافي المدفوع</Text><Text style={styles.studentCommandMiniHint}>{subscriptionDueDate ? `استحقاق ${subscriptionDueDate}` : "لا يوجد تاريخ استحقاق"}</Text></View>
      </View>

      <SectionHeader title="تفاصيل الملف" subtitle="البيانات والمواد والاشتراك والحصص والدرجات والواجبات والملاحظات" />
      <InputField label="الاسم" value={name} onChangeText={setName} />
'''
if 'STUDENT COMMAND CENTER' not in s:
    if jsx_anchor not in s:
        raise SystemExit('jsx anchor not found')
    s = s.replace(jsx_anchor, jsx_insert, 1)

styles_anchor = '  profileSummary: { flexDirection: "row-reverse", alignItems: "center", gap: 10, backgroundColor: COLORS.sage, borderRadius: 18, padding: 14 },'
styles_insert = '''  studentCommandHero: { backgroundColor: COLORS.primaryDeep, borderRadius: 25, padding: 16, borderWidth: 1, borderColor: "rgba(200,161,90,0.42)", shadowColor: COLORS.primaryDeep, shadowOpacity: 0.12, shadowOffset: { width: 0, height: 8 }, shadowRadius: 18, elevation: 3 },
  studentCommandHeroTop: { flexDirection: "row-reverse", alignItems: "center", gap: 10 },
  studentCommandAvatar: { width: 52, height: 52, borderRadius: 17, backgroundColor: COLORS.champagne, alignItems: "center", justifyContent: "center", borderWidth: 2, borderColor: "rgba(255,255,255,0.24)" },
  studentCommandAvatarText: { color: COLORS.primaryDeep, fontSize: 23, fontWeight: "900" },
  studentCommandEyebrow: { color: COLORS.champagne, fontSize: 8, fontWeight: "900", letterSpacing: 1.2, textAlign: "right" },
  studentCommandName: { color: "#FFFFFF", fontSize: 21, fontWeight: "900", marginTop: 3, textAlign: "right", writingDirection: "rtl" },
  studentCommandMeta: { color: "#C8D8D2", fontSize: 10, marginTop: 3, textAlign: "right", writingDirection: "rtl" },
  studentStatusPill: { flexDirection: "row-reverse", alignItems: "center", gap: 5, paddingHorizontal: 8, paddingVertical: 6, borderRadius: 12, alignSelf: "flex-start" },
  studentStatusDot: { width: 6, height: 6, borderRadius: 3 },
  studentStatusText: { color: "#E9F0EC", fontSize: 9, fontWeight: "900" },
  studentCommandDivider: { height: 1, backgroundColor: "rgba(255,255,255,0.12)", marginVertical: 14 },
  studentCommandKpis: { flexDirection: "row-reverse", alignItems: "stretch" },
  studentCommandKpi: { flex: 1, alignItems: "center", gap: 2 },
  studentCommandKpiValue: { color: "#FFFFFF", fontSize: 14, fontWeight: "900", textAlign: "center" },
  studentCommandKpiLabel: { color: "#BFD0C9", fontSize: 8, fontWeight: "700", textAlign: "center" },
  studentCommandKpiDivider: { width: 1, backgroundColor: "rgba(255,255,255,0.12)" },
  studentCommandProgressCard: { backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, borderRadius: 20, padding: 13, gap: 7 },
  studentCommandSection: { backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, borderRadius: 20, padding: 13, gap: 9 },
  studentCommandSectionHeader: { flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between" },
  studentCommandSectionTitleRow: { flexDirection: "row-reverse", alignItems: "center", justifyContent: "space-between" },
  studentCommandSectionTitle: { color: COLORS.ink, fontSize: 13, fontWeight: "900", textAlign: "right", writingDirection: "rtl" },
  studentCommandSectionValue: { color: COLORS.primaryDeep, fontSize: 13, fontWeight: "900" },
  studentCommandCount: { color: COLORS.muted, fontSize: 9, fontWeight: "800" },
  studentCommandProgressTrack: { height: 8, borderRadius: 5, backgroundColor: COLORS.sageSoft, overflow: "hidden" },
  studentCommandProgressFill: { height: 8, borderRadius: 5, backgroundColor: COLORS.champagne },
  studentCommandHint: { color: COLORS.muted, fontSize: 9, textAlign: "right", writingDirection: "rtl" },
  studentCommandChipWrap: { flexDirection: "row-reverse", flexWrap: "wrap", gap: 6 },
  studentCommandChip: { backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: COLORS.border, borderRadius: 12, paddingHorizontal: 9, paddingVertical: 6 },
  studentCommandChipText: { color: COLORS.primaryDeep, fontSize: 9, fontWeight: "800", textAlign: "right", writingDirection: "rtl" },
  studentCommandListRow: { flexDirection: "row-reverse", alignItems: "center", gap: 9, borderTopWidth: 1, borderTopColor: COLORS.border, paddingTop: 9 },
  studentCommandRowIcon: { width: 34, height: 34, borderRadius: 11, backgroundColor: COLORS.sage, alignItems: "center", justifyContent: "center" },
  studentCommandRowTitle: { color: COLORS.ink, fontSize: 11, fontWeight: "900", textAlign: "right", writingDirection: "rtl" },
  studentCommandRowSub: { color: COLORS.muted, fontSize: 9, marginTop: 2, textAlign: "right", writingDirection: "rtl" },
  studentCommandNextBadge: { minWidth: 66, paddingHorizontal: 7, paddingVertical: 6, borderRadius: 11, backgroundColor: COLORS.sageSoft, borderWidth: 1, borderColor: COLORS.border, alignItems: "center" },
  studentCommandNextBadgeText: { color: COLORS.primaryDeep, fontSize: 8, fontWeight: "900" },
  studentCommandNextTime: { color: COLORS.champagne, fontSize: 10, fontWeight: "900", marginTop: 2 },
  studentCommandMiniGrid: { flexDirection: "row-reverse", flexWrap: "wrap", gap: 8 },
  studentCommandMiniCard: { width: "48.5%", minHeight: 105, backgroundColor: COLORS.surface, borderWidth: 1, borderColor: COLORS.border, borderRadius: 18, padding: 11, alignItems: "flex-end" },
  studentCommandMiniIcon: { width: 31, height: 31, borderRadius: 10, alignItems: "center", justifyContent: "center", marginBottom: 7 },
  studentCommandMiniValue: { color: COLORS.ink, fontSize: 16, fontWeight: "900", textAlign: "right" },
  studentCommandMiniLabel: { color: COLORS.muted, fontSize: 9, fontWeight: "800", marginTop: 2, textAlign: "right", writingDirection: "rtl" },
  studentCommandMiniHint: { color: COLORS.primaryDeep, fontSize: 8, fontWeight: "700", marginTop: 4, textAlign: "right", writingDirection: "rtl" },
'''
if 'studentCommandHero:' not in s:
    if styles_anchor not in s:
        raise SystemExit('styles anchor not found')
    s = s.replace(styles_anchor, styles_insert + styles_anchor, 1)

app.write_text(s)
