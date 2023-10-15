Codes = {
    100: {
        "ru": "Сервер сайта удовлетворён начальными сведениями о запросе, клиент может продолжать пересылать заголовки.",
        "en": "This interim response indicates that the client should continue the request or ignore the response if the request is already finished.",
    },
    101: {
        "ru": "Сервер сайта выполняет требование клиента и переключает протоколы в соответствии с указанием, данным в поле заголовка Upgrade. Сервер отправляет заголовок ответа Upgrade, указывая протокол, на который он переключился.",
        "en": "This code is sent in response to an Upgrade request header from the client and indicates the protocol the server is switching to.",
    },
    102: {
        "ru": "Запрос на сайте принят, но на его обработку понадобится длительное время. Используется сервером, чтобы клиент не разорвал соединение из-за превышения времени ожидания. Клиент при получении такого ответа должен сбросить таймер и дожидаться следующей команды в обычном режиме.",
        "en": "This code indicates that the server has received and is processing the request, but no response is available yet."
    },
    103: {
        "ru": "Используется для раннего возврата части заголовков, когда заголовки полного ответа не могут быть быстро сформированы.",
        "en": "This status code is primarily intended to be used with the Link header, letting the user agent start preloading resources while the server prepares a response."
    },
    200: {
        "ru": "Успешный запрос. Если клиентом были запрошены какие-либо данные, то они находятся в заголовке и/или теле сообщения. Сайт отвечает на все запросы и работает исправно.",
        "en": "The request succeeded."
    },
    201: {
        "ru": "В результате успешного выполнения запроса был создан новый ресурс. Сервер может указать адреса (их может быть несколько) созданного ресурса в теле ответа, при этом предпочтительный адрес указывается в заголовке Location",
        "en": "The request succeeded, and a new resource was created as a result. This is typically the response sent after POST requests, or some PUT requests."
    },
    202: {
        "ru": "Запрос был принят на обработку, но она не завершена. Клиенту не обязательно дожидаться окончательной передачи сообщения, так как может быть начат очень долгий процесс.",
        "en": "The request has been received but not yet acted upon. It is noncommittal, since there is no way in HTTP to later send an asynchronous response indicating the outcome of the request. It is intended for cases where another process or server handles the request, or for batch processing. "
    },
    203: {
        "ru": "Аналогично ответу 200 (все работает исправно), но в этом случае передаваемая информация была взята не из первичного источника (резервной копии, другого сервера и т. д.) и поэтому может быть неактуальной.",
        "en": "This response code means the returned metadata is not exactly the same as is available from the origin server, but is collected from a local or a third-party copy. This is mostly used for mirrors or backups of another resource. Except for that specific case, the 200 OK response is preferred to this status. "
    },
    204: {
        "ru": "Сервер успешно обработал запрос, но в ответе были переданы только заголовки без тела сообщения. Клиент не должен обновлять содержимое документа, но может применить к нему полученные метаданные.",
        "en": "There is no content to send for this request, but the headers may be useful. The user agent may update its cached headers for this resource with the new ones."
    },
    205: {
        "ru": "Сервер обязывает клиента сбросить введённые пользователем данные. Тела сообщения сервер при этом не передаёт и документ обновлять не обязательно.",
        "en": "Tells the user agent to reset the document which sent this request."
    },
    206: {
        "ru": "Сервер удачно выполнил частичный GET-запрос, возвратив только часть сообщения. В заголовке Content-Range сервер указывает байтовые диапазоны содержимого. Особое внимание при работе с подобными ответами следует уделить кэшированию.",
        "en": "This response code is used when the Range header is sent from the client to request only part of a resource."
    },
    207: {
        "ru": "Сервер передаёт результаты выполнения сразу нескольких независимых операций. Они помещаются в само тело сообщения в виде XML-документа с объектом multistatus. Не рекомендуется размещать в этом объекте статусы из серии 1xx из-за бессмысленности и избыточности.",
        "en": "Conveys information about multiple resources, for situations where multiple status codes might be appropriate."
    },
    208: {
        "ru": "Члены привязки DAV уже были перечислены в предыдущей части (multistatus) ответа и не включаются снова.",
        "en": "Used inside a <dav:propstat> response element to avoid repeatedly enumerating the internal members of multiple bindings to the same collection."
    },
    226: {
        "ru": "Заголовок A-IM от клиента был успешно принят и сервер возвращает содержимое с учётом указанных параметров. Введено в RFC 3229 для дополнения протокола HTTP поддержкой дельта-кодирования.",
        "en": "The server has fulfilled a GET request for the resource, and the response is a representation of the result of one or more instance-manipulations applied to the current instance."
    },
    300: {
        "ru": "По указанному URI существует несколько вариантов предоставления ресурса по типу MIME, по языку или по другим характеристикам. Сервер передаёт с сообщением список альтернатив, давая возможность сделать выбор клиенту автоматически или пользователю.",
        "en": "The request has more than one possible response. The user agent or user should choose one of them. (There is no standardized way of choosing one of the responses, but HTML links to the possibilities are recommended so the user can pick.)"
    },
    301: {
        "ru": "Запрошенный документ был окончательно перенесен на новый URI, указанный в поле Location заголовка. Некоторые клиенты некорректно ведут себя при обработке данного кода.",
        "en": "The URL of the requested resource has been changed permanently. The new URL is given in the response."
    },
    302: {
        "ru": "Запрошенный документ временно доступен по другому URI, указанному в заголовке в поле Location. Этот код может быть использован, например, при управляемом сервером согласовании содержимого. Некоторые[какие?] клиенты некорректно ведут себя при обработке данного кода.",
        "en": "This response code means that the URI of requested resource has been changed temporarily. Further changes in the URI might be made in the future. Therefore, this same URI should be used by the client in future requests. "
    },
    303: {
        "ru": "Документ по запрошенному URI нужно запросить по адресу в поле Location заголовка с использованием метода GET несмотря даже на то, что первый запрашивался иным методом. Этот код был введён вместе с кодом 307 для избежания неоднозначности, чтобы сервер был уверен, что следующий ресурс будет запрошен методом GET. Например, на веб-странице есть поле ввода текста для быстрого перехода и поиска. После ввода данных браузер делает запрос методом POST, включая в тело сообщения введённый текст. Если обнаружен документ с введённым названием, то сервер отвечает кодом 303, указав в заголовке Location его постоянный адрес. Тогда браузер гарантировано его запросит методом GET для получения содержимого. В противном случае сервер просто вернёт клиенту страницу с результатами поиска.",
        "en": "The server sent this response to direct the client to get the requested resource at another URI with a GET request."
    },
    304: {
        "ru": "Сервер возвращает такой код, если клиент запросил документ методом GET, использовал заголовок If-Modified-Since или If-None-Match и документ не изменился с указанного момента. При этом сообщение сервера не должно содержать тела.",
        "en": "This is used for caching purposes. It tells the client that the response has not been modified, so the client can continue to use the same cached version of the response. "
    },
    305: {
        "ru": "Запрос к запрашиваемому ресурсу должен осуществляться через прокси-сервер, URI которого указан в поле Location заголовка. Данный код ответа могут использовать только исходные HTTP-сервера (не прокси).",
        "en": "Defined in a previous version of the HTTP specification to indicate that a requested response must be accessed by a proxy. It has been deprecated due to security concerns regarding in-band configuration of a proxy. "
    },
    306: {
        "ru": "Использовавшийся в ранних версиях спецификации код ответа, в настоящий момент зарезервирован. Упомянут в RFC 2616 (обновление HTTP/1.1). Согласно ранним наброскам, код означал Switch Proxy, указывая клиенту сменить используемый прокси-сервер на указанный сервером в заголовке ответа.",
        "en": "This response code is no longer used; it is just reserved. It was used in a previous version of the HTTP/1.1 specification."
    },
    307: {
        "ru": "Запрашиваемый ресурс на короткое время доступен по другому URI, указанный в поле Location заголовка. Метод запроса (GET/POST) менять не разрешается. Например, POST-запрос должен быть отправлен по новому URI тем же методом POST. Этот код был введён вместе с 303-м вместо 302-го для избежания неоднозначности.",
        "en": "The server sends this response to direct the client to get the requested resource at another URI with same method that was used in the prior request. This has the same semantics as the 302 Found HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request."
    },
    308: {
        "ru": "Запрашиваемый ресурс был окончательно перенесен на новый URI, указанный в поле Location заголовка. Метод запроса (GET/POST) менять не разрешается. Например, POST-запрос должен быть отправлен по новому URI тем же методом POST. Этот код был введён вместо 301-го для избежания неоднозначности.",
        "en": "This means that the resource is now permanently located at another URI, specified by the Location: HTTP Response header. This has the same semantics as the 301 Moved Permanently HTTP response code, with the exception that the user agent must not change the HTTP method used: if a POST was used in the first request, a POST must be used in the second request. "
    },
    400: {
        "ru": "Сервер обнаружил в запросе клиента синтаксическую ошибку.",
        "en": "The server cannot or will not process the request due to something that is perceived to be a client error (e.g., malformed request syntax, invalid request message framing, or deceptive request routing)."
    },
    401: {
        "ru": "Для доступа к запрашиваемому ресурсу требуется аутентификация. В заголовке ответ должен содержать поле WWW-Authenticate с перечнем условий аутентификации. Иными словами, для доступа к запрашиваемому ресурсу клиент должен представиться, послав запрос, включив при этом в заголовок сообщения поле Authorization с требуемыми для аутентификации данными. Если запрос уже включает данные для авторизации, ответ 401 означает, что в авторизации с ними отказано.",
        "en": "Although the HTTP standard specifies unauthorized, semantically this response means unauthenticated. That is, the client must authenticate itself to get the requested response."
    },
    402: {
        "ru": "Предполагается использовать в будущем. В настоящий момент не используется. Этот код предусмотрен для платных пользовательских сервисов, а не для хостинговых компаний. Имеется в виду, что эта ошибка не будет выдана хостинговым провайдером в случае просроченной оплаты его услуг.",
        "en": "This response code is reserved for future use. The initial aim for creating this code was using it for digital payment systems, however this status code is used very rarely and no standard convention exists. "
    },
    403: {
        "ru": "Сервер понял запрос, но он отказывается его выполнять из-за ограничений в доступе для клиента к указанному ресурсу. Иными словами, клиент не уполномочен совершать операции с запрошенным ресурсом. Если для доступа к ресурсу требуется аутентификация средствами HTTP, то сервер вернёт ответ 401, или 407 при использовании прокси. В противном случае ограничения были заданы администратором сервера или разработчиком веб-приложения и могут быть любыми в зависимости от возможностей используемого программного обеспечения. В любом случае серверу следует сообщить причины отказа в обработке запроса. Наиболее вероятными причинами ограничения может послужить попытка доступа к системным ресурсам веб-сервера (например, файлам .htaccess или .htpasswd) или к файлам, доступ к которым был закрыт с помощью конфигурационных файлов, требование аутентификации не средствами HTTP, например, для доступа к системе управления содержимым или разделу для зарегистрированных пользователей либо сервер не удовлетворён IP-адресом клиента, например, при блокировках.",
        "en": "The client does not have access rights to the content; that is, it is unauthorized, so the server is refusing to give the requested resource. Unlike 401 Unauthorized, the client's identity is known to the server. "
    },
    404: {
        "ru": "Самая распространённая ошибка при пользовании Интернетом, основная причина — ошибка в написании адреса Web-страницы. Сервер понял запрос, но не нашёл соответствующего ресурса по указанному URL. Если серверу известно, что по этому адресу был документ, то ему желательно использовать код 410. Ответ 404 может использоваться вместо 403, если требуется тщательно скрыть от посторонних глаз определённые ресурсы.",
        "en": "The server cannot find the requested resource. In the browser, this means the URL is not recognized. In an API, this can also mean that the endpoint is valid but the resource itself does not exist. Servers may also send this response instead of 403 Forbidden to hide the existence of a resource from an unauthorized client. This response code is probably the most well known due to its frequent occurrence on the web."
    },
    405: {
        "ru": "Указанный клиентом метод нельзя применить к текущему ресурсу. В ответе сервер должен указать доступные методы в заголовке Allow, разделив их запятой. Эту ошибку сервер должен возвращать, если метод ему известен, но он не применим именно к указанному в запросе ресурсу, если же указанный метод не применим на всём сервере, то клиенту нужно вернуть код 501 (Not Implemented).",
        "en": "The request method is known by the server but is not supported by the target resource. For example, an API may not allow calling DELETE to remove a resource. "
    },
    406: {
        "ru": "Запрошенный URI не может удовлетворить переданным в заголовке характеристикам. Если метод был не HEAD, то сервер должен вернуть список допустимых характеристик для данного ресурса.",
        "en": "This response is sent when the web server, after performing server-driven content negotiation, doesn't find any content that conforms to the criteria given by the user agent."
    },
    407: {
        "ru": "Ответ аналогичен коду 401 за исключением того, что аутентификация производится для прокси-сервера. Механизм аналогичен идентификации на исходном сервере.",
        "en": "This is similar to 401 Unauthorized but authentication is needed to be done by a proxy."
    },
    408: {
        "ru": "Время ожидания сервером передачи от клиента истекло. Клиент может повторить аналогичный предыдущему запрос в любое время. Например, такая ситуация может возникнуть при загрузке на сервер объёмного файла методом POST или PUT. В какой-то момент передачи источник данных перестал отвечать, например, из-за повреждения компакт-диска или потери связи с другим компьютером в локальной сети. Пока клиент ничего не передаёт, ожидая от него ответа, соединение с сервером держится. Через некоторое время сервер может закрыть соединение со своей стороны, чтобы дать возможность другим клиентам сделать запрос. Этот ответ не возвращается, когда клиент принудительно остановил передачу по команде пользователя или соединение прервалось по каким-то иным причинам, так как ответ уже послать невозможно.",
        "en": "This response is sent on an idle connection by some servers, even without any previous request by the client. It means that the server would like to shut down this unused connection. This response is used much more since some browsers, like Chrome, Firefox 27+, or IE9, use HTTP pre-connection mechanisms to speed up surfing. Also note that some servers merely shut down the connection without sending this message. "
    },
    409: {
        "ru": "Запрос не может быть выполнен из-за конфликтного обращения к ресурсу. Такое возможно, например, когда два клиента пытаются изменить ресурс с помощью метода PUT.",
        "en": "This response is sent when a request conflicts with the current state of the server."
    },
    410: {
        "ru": "Такой ответ сервер посылает, если ресурс раньше был по указанному URL, но был удалён и теперь недоступен. Серверу в этом случае неизвестно и местоположение альтернативного документа (например копии).",
        "en": "This response is sent when the requested content has been permanently deleted from server, with no forwarding address. Clients are expected to remove their caches and links to the resource. APIs should not feel compelled to indicate resources that have been deleted with this status code."
    },
    411: {
        "ru": "Для указанного ресурса клиент должен указать Content-Length в заголовке запроса. Без указания этого поля не стоит делать повторную попытку запроса к серверу по данному URI. Такой ответ естественен для запросов типа POST и PUT. Например, если по указанному URI производится загрузка файлов, а на сервере стоит ограничение на их объём. Тогда разумней будет проверить в самом начале заголовок Content-Length и сразу отказать в загрузке, чем провоцировать бессмысленную нагрузку, разрывая соединение, когда клиент действительно пришлёт слишком объёмное сообщение.",
        "en": "Server rejected the request because the Content-Length header field is not defined and the server requires it."
    },
    412: {
        "ru": "Возвращается, если ни одно из условных полей заголовка (If-Match и др., см. RFC 7232) запроса не было выполнено.",
        "en": "The client has indicated preconditions in its headers which the server does not meet."
    },
    413: {
        "ru": "Возвращается в случае, если сервер отказывается обработать запрос по причине слишком большого размера тела запроса. Сервер может закрыть соединение, чтобы прекратить дальнейшую передачу запроса. Если проблема временная, то рекомендуется в ответ сервера включить заголовок Retry-After с указанием времени, по истечении которого можно повторить аналогичный запрос.",
        "en": "Request entity is larger than limits defined by server. The server might close the connection or return an Retry-After header field."
    },
    414: {
        "ru": "Сервер не может обработать запрос из-за слишком длинного указанного URI. Такую ошибку можно спровоцировать, например, когда клиент пытается передать длинные параметры через метод GET, а не POST.",
        "en": "The URI requested by the client is longer than the server is willing to interpret."
    },
    415: {
        "ru": "По каким-то причинам сервер отказывается работать с указанным типом данных при данном методе.",
        "en": "The media format of the requested data is not supported by the server, so the server is rejecting the request."
    },
    416: {
        "ru": "В поле Range заголовка запроса был указан диапазон за пределами ресурса и отсутствует поле If-Range. Если клиент передал байтовый диапазон, то сервер может вернуть реальный размер в поле Content-Range заголовка. Данный ответ не следует использовать при передаче типа multipart/byteranges.",
        "en": "The range specified by the Range header field in the request cannot be fulfilled. It's possible that the range is outside the size of the target URI's data. "
    },
    417: {
        "ru": "По каким-то причинам сервер не может удовлетворить значению поля Expect заголовка запроса.",
        "en": "This response code means the expectation indicated by the Expect request header field cannot be met by the server."
    },
    418: {
        "ru": "Этот код был введен в 1998 году как одна из традиционных первоапрельских шуток IETF в RFC 2324, Hyper Text Coffee Pot Control Protocol. Не ожидается, что данный код будет поддерживаться реальными серверами.",
        "en": "The server refuses the attempt to brew coffee with a teapot."
    },
    419: {
        "ru": "Этого кода нет в RFC 2616, используется в качестве альтернативы коду 401, которые прошли проверку подлинности, но лишены доступа к определенным ресурсам сервера. Обычно код отдается, если CSRF-токен устарел или оказался некорректным.",
        "en": "Session has expired while processing a post request"
    },
    421: {
        "ru": "Запрос был перенаправлен на сервер, не способный дать ответ.",
        "en": "The request was directed at a server that is not able to produce a response. This can be sent by a server that is not configured to produce responses for the combination of scheme and authority that are included in the request URI."
    },
    422: {
        "ru": "Сервер успешно принял запрос, может работать с указанным видом данных (например, в теле запроса находится XML-документ, имеющий верный синтаксис), однако имеется какая-то логическая ошибка, из-за которой невозможно произвести операцию над ресурсом.",
        "en": "The request was well-formed but was unable to be followed due to semantic errors."
    },
    423: {
        "ru": "Целевой ресурс из запроса заблокирован от применения к нему указанного метода.",
        "en": "The resource that is being accessed is locked."
    },
    424: {
        "ru": "Реализация текущего запроса может зависеть от успешности выполнения другой операции. Если она не выполнена и из-за этого нельзя выполнить текущий запрос, то сервер вернёт этот код.",
        "en": "The request failed due to failure of a previous request."
    },
    425: {
        "ru": "Сервер не готов принять риски обработки 'ранней информации'.",
        "en": "Indicates that the server is unwilling to risk processing a request that might be replayed."
    },
    426: {
        "ru": "Сервер указывает клиенту на необходимость обновить протокол. Заголовок ответа должен содержать правильно сформированные поля Upgrade и Connection.",
        "en": "The server refuses to perform the request using the current protocol but might be willing to do so after the client upgrades to a different protocol. The server sends an Upgrade header in a 426 response to indicate the required protocol(s). "
    },
    428: {
        "ru": "Сервер указывает клиенту на необходимость использования в запросе заголовков условий, наподобие If-Match.",
        "en": "The origin server requires the request to be conditional. This response is intended to prevent the 'lost update' problem, where a client GETs a resource's state, modifies it and PUTs it back to the server, when meanwhile a third party has modified the state on the server, leading to a conflict."
    },
    429: {
        "ru": "Клиент попытался отправить слишком много запросов за короткое время, что может указывать, например, на попытку DDoS-атаки. Может сопровождаться заголовком Retry-After, указывающим, через какое время можно повторить запрос.",
        "en": "The user has sent too many requests in a given amount of time."
    },
    431: {
        "ru": "Превышена допустимая длина заголовков. Сервер не обязан отвечать этим кодом, вместо этого он может просто сбросить соединение.",
        "en": "The server is unwilling to process the request because its header fields are too large. The request may be resubmitted after reducing the size of the request header fields. "
    },
    434: {
        "ru": "Запрашиваемый адрес недоступен",
        "en": "Requested host unavailable."
    },
    449: {
        "ru": "Возвращается сервером, если для обработки запроса от клиента поступило недостаточно информации. При этом в заголовок ответа помещается поле Ms-Echo-Request.",
        "en": "request cannot be satisfied because insufficient information was provided by the client."
    },
    451: {
        "ru": "Доступ к ресурсу закрыт по юридическим причинам, например, по требованию органов государственной власти или по требованию правообладателя в случае нарушения авторских прав.",
        "en:": "The user agent requested a resource that cannot legally be provided, such as a web page censored by a government"
    },
    499: {
        "ru": "Нестандартный код, предложенный и используемый nginx для случаев, когда клиент закрыл соединение, пока nginx обрабатывал запрос.",
        "en": "Indicates that the client has closed the connection while the server is still processing the request."
    },
    500: {
        "ru": "Любая внутренняя ошибка сервера, которая не входит в рамки остальных ошибок класса.",
        "en": "The server has encountered a situation it does not know how to handle."
    },
    501: {
        "ru": "Сервер не поддерживает возможностей, необходимых для обработки запроса. Типичный ответ для случаев, когда сервер не понимает указанный в запросе метод. Если же метод серверу известен, но он не применим к данному ресурсу, то нужно вернуть ответ 405.",
        "en": "The request method is not supported by the server and cannot be handled. The only methods that servers are required to support (and therefore that must not return this code) are GET and HEAD."
    },
    502: {
        "ru": "Сервер, выступая в роли шлюза или прокси-сервера, получил недействительное ответное сообщение от вышестоящего сервера.",
        "en": "This error response means that the server, while working as a gateway to get a response needed to handle the request, got an invalid response."
    },
    503: {
        "ru": "Сервер временно не имеет возможности обрабатывать запросы по техническим причинам (обслуживание, перегрузка и прочее). В поле Retry-After заголовка сервер может указать время, через которое клиенту рекомендуется повторить запрос. Хотя во время перегрузки очевидным кажется сразу разрывать соединение, эффективней может оказаться установка большого значения поля Retry-After для уменьшения частоты избыточных запросов.",
        "en": "The server is not ready to handle the request. Common causes are a server that is down for maintenance or that is overloaded. Note that together with this response, a user-friendly page explaining the problem should be sent. This response should be used for temporary conditions and the Retry-After HTTP header should, if possible, contain the estimated time before the recovery of the service. The webmaster must also take care about the caching-related headers that are sent along with this response, as these temporary condition responses should usually not be cached."
    },
    504: {
        "ru": "Сервер в роли шлюза или прокси-сервера не дождался ответа от вышестоящего сервера для завершения текущего запроса.",
        "en": "This error response is given when the server is acting as a gateway and cannot get a response in time."
    },
    505: {
        "ru": "Сервер не поддерживает или отказывается поддерживать указанную в запросе версию протокола HTTP.",
        "en": "The HTTP version used in the request is not supported by the server."
    },
    506: {
        "ru": "В результате ошибочной конфигурации выбранный вариант указывает сам на себя, из-за чего процесс связывания прерывается.",
        "en": "The server has an internal configuration error: the chosen variant resource is configured to engage in transparent content negotiation itself, and is therefore not a proper end point in the negotiation process."
    },
    507: {
        "ru": "Не хватает места для выполнения текущего запроса. Проблема может быть временной.",
        "en": "The method could not be performed on the resource because the server is unable to store the representation needed to successfully complete the request."
    },
    508: {
        "ru": "Операция отменена, т.к. сервер обнаружил бесконечный цикл при обработке запроса без ограничения глубины. Бывает, что появляется при исчерпании лимитов хостинга.",
        "en": "The server detected an infinite loop while processing the request."
    },
    509: {
        "ru": "Используется при превышении веб-площадкой отведённого ей ограничения на потребление трафика. В данном случае владельцу площадки следует обратиться к своему хостинг-провайдеру.",
        "en": "It interrupts the displaying of your website to your visitors. The only thing that they can see is a blank page infroming about the bandwidth limit being exceeded."
    },
    510: {
        "ru": "На сервере отсутствует расширение, которое желает использовать клиент. Сервер может дополнительно передать информацию о доступных ему расширениях.",
        "en": "Further extensions to the request are required for the server to fulfill it."
    },
    511: {
        "ru": "Тот ответ посылается не сервером, которому был предназначен запрос, а сервером-посредником — например, сервером провайдера — в случае, если клиент должен сначала авторизоваться в сети, например, ввести пароль для платной точки доступа к Интернету. Предполагается, что в теле ответа будет возвращена Web-форма авторизации или перенаправление на неё.",
        "en": "Indicates that the client needs to authenticate to gain network access. This status is not generated by origin servers, but by intercepting proxies that control access to the network"
    },
    520: {
        "ru": "Возникает когда сервер CDN не смог обработать ошибку веб-сервера.",
        "en": "Happens when the web server receives an invalid or incorrectly interpreted request, prompting an empty response."
    },
    521: {
        "ru": "Возникает когда подключения CDN отклоняются веб-сервером.",
        "en": "Error 521 is a Cloudflare-specific error message. It means that your web browser was able to successfully connect to Cloudflare, but Cloudflare was not able to connect to the origin web server. 525: “SSL Handshake Failed“."
    },
    522: {
        "ru": "Возникает когда CDN не удалось подключиться к веб-серверу.",
        "en": "The server has reached the maximum limit Firewall has blocked a Cloudflare IP address Incorrect IP address KeepAlive disabled"
    },
    523: {
        "ru": "Возникает когда веб-сервер недостижим.",
        "en": "Occurs when there is an error with the origin server and it cannot be reached."
    },
    524: {
        "ru": "Возникает при истечении тайм-аута подключения между сервером CDN и веб-сервером.",
        "en": "Indicates that Cloudflare successfully connected to the origin web server, but the origin did not provide an HTTP response before the default 100 second connection timed out."
    },
    525: {
        "ru": "Возникает при ошибке рукопожатия SSL между сервером CDN и веб-сервером.",
        "en":  "Means that the server and browser were unable to establish a secure connection."
    },
    526: {
        "ru": "Возникает когда не удаётся подтвердить сертификат шифрования веб-сервера.",
        "en": "Indicates Cloudflare is unable to successfully validate the SSL certificate on the origin web server and the SSL setting in the Cloudflare SSL/TLS app is set to Full SSL (Strict) for the website. When this happens, you'll see “Error 526: Invalid SSL certificate”."
    }
};
