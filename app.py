# ==========================================
# 2. EREBUS ORACLE UI (FRONTEND TEMPLATE)
# ==========================================
EREBUS_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Erebus | Nuka-Strike Active</title>
    <script src="https://cdn.tailwindcss.com"></script>
</head>
<body class="bg-slate-950 text-white font-sans flex flex-col items-center justify-center min-h-screen p-4">
    
    <div class="w-full max-w-lg bg-slate-900 border border-blue-500/30 p-8 rounded-[2rem] shadow-2xl relative">
        
        <div class="flex gap-2 mb-6 justify-center">
            <div class="text-[10px] font-bold px-3 py-1 rounded-full border bg-blue-600 border-blue-500 uppercase">
                Nuka-Strike Targeting
            </div>
            <div class="text-[10px] font-bold px-3 py-1 rounded-full border border-slate-700 text-slate-400 uppercase">
                Pure Differentials
            </div>
        </div>
        
        <h1 class="text-3xl font-black text-blue-400 mb-6 text-center tracking-tighter uppercase">
            Erebus Engine
        </h1>
        
        <form method="POST" action="/" class="space-y-4 text-sm">
            
            <div class="bg-slate-800 p-4 rounded-xl border border-slate-700 focus-within:border-blue-500/50 transition-colors">
                <label for="elo" class="block text-xs text-slate-400 font-bold mb-1 uppercase">
                    Tier 1: Base Elo Probability (0-100)
                </label>
                <input type="number" id="elo" name="elo" step="0.1" value="{{ request.form.get('elo', 50) }}" required
                    class="w-full bg-slate-900 p-3 rounded outline-none text-white border border-transparent focus:border-blue-500/50 transition-all">
            </div>
            
            <div class="bg-slate-800 p-4 rounded-xl border border-slate-700 focus-within:border-emerald-500/50 transition-colors">
                <label for="eff" class="block text-xs text-slate-400 font-bold mb-1 uppercase">
                    Pure Efficiency Differential
                </label>
                <input type="number" id="eff" name="eff" step="0.1" value="{{ request.form.get('eff', 0) }}" required
                    class="w-full bg-slate-900 p-3 rounded outline-none text-white border border-transparent focus:border-emerald-500/50 transition-all">
            </div>
            
            <div class="bg-slate-800 p-4 rounded-xl border border-slate-700 focus-within:border-red-500/50 transition-colors">
                <label for="injury" class="block text-xs text-slate-400 font-bold mb-1 uppercase">
                    Tier 2: Roster Shift (-50 to 50)
                </label>
                <input type="number" id="injury" name="injury" step="0.1" value="{{ request.form.get('injury', 0) }}" required
                    class="w-full bg-slate-900 p-3 rounded outline-none text-white border border-transparent focus:border-red-500/50 transition-all">
            </div>
            
            <button type="submit" class="w-full bg-blue-600 hover:bg-blue-500 py-4 rounded-xl font-black text-lg transition-all mt-6 uppercase tracking-wide shadow-lg shadow-blue-900/50">
                Calculate Confidence
            </button>
        </form>

        {% if confidence is not none %}
        <div class="mt-8 p-6 bg-black/50 rounded-xl border border-white/10 text-center animate-in fade-in duration-500">
            <div class="text-xs text-slate-400 mb-2 uppercase font-bold tracking-widest">Mission Success Confidence</div>
            <div class="text-5xl font-black {% if confidence >= 70 %}text-emerald-400{% elif confidence >= 50 %}text-blue-400{% else %}text-red-400{% endif %} drop-shadow-md">
                {{ confidence }}%
            </div>
        </div>
        {% endif %}
        
        <div class="mt-6 text-center text-[10px] text-slate-500 uppercase font-bold tracking-widest space-y-1">
            <p><span class="text-red-500">■</span> Regional Modifiers: Disabled</p>
            <p><span class="text-red-500">■</span> Home Field Advantage: Offline</p>
        </div>

    </div>
</body>
</html>
"""