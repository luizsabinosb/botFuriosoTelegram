# coding: utf-8

from telegram import Update, InlineKeyboardMarkup, InlineKeyboardButton
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes

TOKEN = 'TOKEN_UTILIZADO_NO_BOT'

# --- Menu principal ---
def criar_menu():
    botoes = [
        [InlineKeyboardButton("📅 Próximo Jogo", callback_data="proximo_jogo"),
         InlineKeyboardButton("📊 Ranking", callback_data="ranking")],
        [InlineKeyboardButton("🧑‍💻 Line-up", callback_data="lineup"),
         InlineKeyboardButton("🌐 Redes Sociais", callback_data="redes_sociais")],
        [InlineKeyboardButton("📉 Rivais", callback_data="rivais"),
         InlineKeyboardButton("⚔️ Resultado", callback_data="resultado")],
        [InlineKeyboardButton("🛍️ Merch", callback_data="merch")],
        [InlineKeyboardButton("ℹ️ Sobre o Bot", callback_data="sobre")]
    ]
    return InlineKeyboardMarkup(botoes)


def botao_voltar():
    return InlineKeyboardMarkup([[InlineKeyboardButton("🔙 Voltar ao menu", callback_data="menu")]])

# --- Handlers principais ---
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user_first_name = update.effective_user.first_name
    saudacao = f"Salve, <b>{user_first_name}</b>! 🧙‍♂️🔥"
    await update.message.reply_text(
        saudacao + "\n\nEscolha uma opção:",
        reply_markup=criar_menu(),
        parse_mode="HTML"
    )

async def callback_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    # Mostrar carregando...
    await query.edit_message_text(text="⌛ Carregando...", parse_mode="HTML")

    opcoes = {
        "menu": ("Salve novamente! Escolha uma opção:", criar_menu()),
        "proximo_jogo": (buscar_proximo_jogo(), botao_voltar()),
        "ranking": (buscar_ranking(), botao_voltar()),
        "lineup": (buscar_lineup(), botao_voltar()),
        "redes_sociais": (redes_sociais(), botao_voltar()),
        "rivais": (rivais_minimos(), botao_voltar()),
        "resultado": (resultado_recente(), botao_voltar()),
        "merch": (merch_loja(), botao_voltar()),
        "sobre": (sobre_bot(), botao_voltar()),
    }

    texto, teclado = opcoes.get(query.data, ("🤦‍♂️ Opa, não reconhecemos essa opção!", criar_menu()))

    await query.edit_message_text(text=texto, reply_markup=teclado, parse_mode="HTML")

# --- Funções de conteúdo ---
def buscar_proximo_jogo():
    return "<b>📅 Próximo jogo da FURIA:</b>\nAinda sem partidas agendadas. Fique ligado nas atualizações!"

def buscar_ranking():
    return (
        "<b>📊 Ranking Atual:</b>\n"
        "A FURIA está na <b>16ª posição</b> no ranking oficial da HLTV.\n"
        "<a href='https://www.hltv.org/ranking/teams'>Ver ranking completo</a>"
    )

def buscar_lineup():
    return (
        "<b>👥 Line-up atual:</b>\n\n"
        "🔫 <a href='https://www.hltv.org/player/2023/fallen'>FalleN</a>\n"
        "🔫 <a href='https://www.hltv.org/player/12553/yuurih'>yuurih</a>\n"
        "🔫 <a href='https://www.hltv.org/player/15631/kscerato'>KSCERATO</a>\n"
        "🔫 <a href='https://www.hltv.org/player/13915/yekindar'>YEKINDAR</a>\n"
        "🔫 <a href='https://www.hltv.org/player/24144/molodoy'>molodoy</a>\n\n"
        "Estatísticas completas nos perfis HLTV!"
    )

def redes_sociais():
    return (
        "<b>🌐 Redes Sociais FURIA:</b>\n\n"
        "📸 <a href='https://www.instagram.com/furiagg/?hl=pt-br'>Instagram</a>\n"
        "🐦 <a href='https://x.com/FURIA'>Twitter</a>\n"
        "💬 <a href='https://discord.com/invite/furia'>Discord</a>"
    )

def rivais_minimos():
    return (
        "<b>📉 Informativo dos rivais:</b>\n\n"
        "– 🫠 MIBR: Tentando reviver o hype de 2016\n"
        "– 🫥 paiN: Sentem dor contra a FURIA\n"
        "– 😵 Fluxo: Sempre na repescagem\n"
        "– 🐟 Sharks: Afogados em erros\n"
        "– 🪓 O PLANO: Sem plano B\n"
        "– 🧃 RED: Pressiona, mas cai\n\n"
        "Esses não assustam não! 😎"
    )

def resultado_recente():
    return (
        "<b>📊 Últimos Resultados:</b>\n"
        "<a href='https://www.hltv.org/team/8297/furia#tab-matchesBox'>Conferir resultados da FURIA</a>"
    )

def merch_loja():
    return (
        "<b>🛍️ Merch Oficial:</b>\n"
        "<a href='https://www.furia.gg'>Acesse a loja da FURIA</a> para produtos exclusivos!"
    )

def sobre_bot():
    return (
        "<b>ℹ️ Sobre o Bot:</b>\n"
        "Este bot é mantido por torcedores da FURIA e traz atualizações, informações e muito mais!\n"
        "Curtiu? Compartilha com os outros torcedores da Pantera!! z"
    )

# --- Execução do bot ---
app = ApplicationBuilder().token(TOKEN).build()
app.add_handler(CommandHandler("start", start))
app.add_handler(CallbackQueryHandler(callback_handler))
app.run_polling()
