# -*- coding: utf-8 -*-

import telepot
import time

def command_help(chat_id, msg_id):
    bot.sendMessage(chat_id,"""Comandos disponiveis:
/start - Não faz nada de útil;
/divul - mostra links de divulgação do canal;
/regras - mostra as regras;
/save - encaminha a mensagem respondida para seu privado;
/sugestao <sua sugestao> - envia sugestao para novos comandos.
\nAtualmente estou hospedado em um servidor gratuito, por isso o bot pode ficar instável.""", reply_to_message_id = msg_id)

def command_kick(chat_id, msg_id, message):
    try:
        reply_from_id = message['reply_to_message']['from']['id']
        reply_from_name = message['reply_to_message']['from']['first_name']
        from_name = message['from']['first_name']
        bot.kickChatMember(chat_id, reply_from_id)
        bot.unbanChatMember(chat_id, reply_from_id)
        bot.sendMessage(chat_id, "%s foi kickado por %s." % (reply_from_name, from_name), reply_to_message_id = msg_id)
    except:
        bot.sendMessage(chat_id, "Algo de errado não está certo.", reply_to_message_id = msg_id)

def command_ban(chat_id, msg_id, message):
    try:
        reply_from_id = message['reply_to_message']['from']['id']
        reply_from_name = message['reply_to_message']['from']['first_name']
        from_name = message['from']['first_name']
        bot.kickChatMember(chat_id, reply_from_id)
        bot.sendMessage(chat_id, "%s foi banido por %s." % (reply_from_name, from_name), reply_to_message_id = msg_id)
    except:
        bot.sendMessage(chat_id, "Algo de errado não está certo.", reply_to_message_id = msg_id)

def command_unban(chat_id, msg_id, messsage):
    bot.unbanChatMember(chat_id, reply_from_id)
    bot.sendMessage(chat_id, "%s foi desbanido." % reply_from_name, reply_to_message_id = msg_id)

def command_id(chat_id, msg_id, message):
    try:
        msg_id = message['reply_to_message']['message_id']
        text = 'Nome: ' + message['reply_to_message']['from']['first_name']
        text += '\nId: ' + str(message['reply_to_message']['from']['id'])
        text += '\nUser: ' + message['reply_to_message']['from']['username']
        bot.sendMessage(chat_id, text, reply_to_message_id = msg_id)
    except:
        bot.sendMessage(chat_id, "Você deve responder alguém para usar esse comando.",
        reply_to_message_id = msg_id)

def command_save(from_id, chat_id, msg_id, msg):

    try:
        msg_reply_id = msg['reply_to_message']['message_id']

        bot.forwardMessage(from_id, chat_id, msg_reply_id)
        bot.sendMessage(chat_id, 'Mensagem salva!', reply_to_message_id = msg_id)
    except:
        bot.sendMessage(chat_id,'Algo de errado não esta certo.', reply_to_message_id = msg_id)

def command_start(chat_id, msg_id):
    bot.sendMessage(chat_id,
    'Olá, Sou um bot em fase de construção!\nPor favor, tenha paciência comigo.\n\nEnvie-me sugestões com o comando /sugestao <sua sugestão>',
    reply_to_message_id = msg_id)

def command_regras(chat_id, msg_id):
    bot.sendMessage(chat_id,
    '''1 - Jamais ofenda o colega de grupo. Este tipo de ação gera banimento automático.

2 - Aqui não é grupo de divulgação! Qualquer tentativa de divulgar outro grupo/canal deve ser previamente comunicada aos administradores, sendo necessário receber a permissão de pelo menos 2 deles.

3 - Regra de Ouro: em hipótese alguma envie qualquer conteúdo de caráter sexual, seja sticker, imagem, gif, vídeo, texto... nada! Respeite os outros membros!

4 - Você é bem vindo aqui, então sinta-se em casa. Converse, conheça os membros. Dúvidas, críticas e/ou sugestões, podem ser enviadas para qualquer administrador.  Somos uma família, o que pudermos fazer para melhorar o convívio, será feito.

5 - Não seja: poser; hater; mal educado; chorão; chato; arrogante; jogador de LOL (zueira). Divirta-se.

6 - Participe das enquetes e votações, assim saberemos qual é a opinião geral de todos vocês!''',
    reply_to_message_id = msg_id)

def command_divul(chat_id, msg_id):
    bot.sendMessage(chat_id,
    '''PARTICIPE DO NOSSO GRUPO SOBRE JOGOS!

O @GrupoQuaseGamer é um grupo dedicado à assuntos variados, desde os nossos amados jogos eletrônicos, até assuntos polêmicos, como aborto, política e religião.

Melhor lugar pra quem quer falar sobre aquele jogo que marcou a infância, ou pedir dicas daquele jogo que tá te tirando a paciência pra zerar!

Todos são bem vindos, no entanto, é necessário seguir nossas regras básicas para manter o grupo em perfeito funcionamento! Ao entrar, digite /regras@quasebot

Nosso Link: Telegram.me/grupoquasegamer''',
    reply_to_message_id = msg_id)

def find_me(chat_id, msg_id, from_user, msg):
    try:
        chat_name = msg['chat']['title']
        bot.sendMessage(189922184, 'Por %s em %s:' % (from_user, chat_name))
        bot.forwardMessage(189922184, chat_id, msg_id)
    except:
        bot.sendMessage(189922184,
        'Mestre me desculpe!\nMandaram uma sugestão em algum grupo mas ocorreu algum erro e perdi a mensagem.')

def handle(msg):
    try:
        command = msg['text']
    except:
        command = "<ARQUIVO>"
    try:
        from_user = "#" + msg['from']['username']
    except:
        from_user = msg['from']['first_name']
    msg_id = msg['message_id']
    chat_type = msg['chat']['type']
    chat_id = msg['chat']['id']
    from_id = msg['from']['id']
    try:
        adms = bot.getChatAdministrators(chat_id)
    except:
        adms = ''

    print('Got command: %s in %s:%s per %s' % (command, chat_id, chat_type, from_user))

    if command == '/remover' and str(from_id) in str(adms):
        command_kick(chat_id, msg_id, msg)
    elif command == '/banir' and str(from_id) in str(adms):
        command_ban(chat_id, msg_id, msg)
    elif command == '/desbanir' and str(from_id) in str(adms):
        command_unban(chat_id, msg_id, msg)
    elif command =='/start' or (command == '/start@QuaseQuaseBot'):
        command_start(chat_id, msg_id)
    elif command == '/id' or (command == '/id@QuaseQuaseBot'):
        command_id(chat_id, msg_id, msg)
    elif command == '/save' or (command == '/save@QuaseQuaseBot'):
        command_save(from_id, chat_id, msg_id, msg)
    elif command == '/help' or (command == '/help@QuaseQuaseBot'):
        command_help(chat_id, msg_id)
    elif (command == '/sugestao') or (command == '/sugestao@QuaseQuaseBot'):
        find_me(chat_id, msg_id, from_user, msg)
    elif command == '/regras' or (command == '/regras@QuaseQuaseBot'):
        command_regras(chat_id, msg_id)
    elif command == '/divul' or (command == '/divul@QuaseQuaseBot'):
        command_divul(chat_id, msg_id)

bot = telepot.Bot('380172470:AAGCV43qCbLP6SQy4l7DaeS4P0NXXOaeXk4')
bot.message_loop(handle)

print('Executando ...')

while 1:
    time.sleep(10)
