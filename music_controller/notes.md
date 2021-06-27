## Notes
 * server automatic update kalau kita buat apa2 perubahan
 * request pergi ke main urls project dulu baru dia bawak ke urls dlm app
 * backend - a server that can handle request and give some valid respond \
 * Buat satu endpoint supaya frontend boleh tahu room mana yang created
 * Mungkin backend tak hantar frontend HTML code. tapi akan hantar data
 * Serializer , amek data dalam bentuk python daripada model dan translate jadi bentuk json
 View already setup untuk bagi kita ll sort of different view
 * MAcam ni lah rest api di setup
 * MAcam mana nak add react
 All stuff related to frontend
 * static, apa2 yang browser akan cache
 * main javascript bundle
 * webpack untuk transpile semuajs  src file / bundle smua src file dalam satu file.
 * Babel untuk transpile code kita jadi any-browser friendly
 npm i @babel/core babel-loader @babel/preset-env @babel/preset-react --save-dev
 * Install React
 * Install Material UI : Prebuilt component supaya kita takyah style webpage sendiri.
 * Install Babel punya plugin : npm install @babel/plugin-proposal-class-properties
 * Untuk bagi kita boleh guna async dan await dalam kita pnya code.
 * Untuk bagi kita reroute from different pages. : npm install react-router-dom
* Setup configuration script yang akan run  dan uruskan webpack, babel dan smua.
* link : https://github.com/techwithtim/Music-Controller-Web-App-Tutorial/blob/main/Tutorial%201%20-%204/frontend/babel.config.json 
* babel.config.json/rc setup kan babel loader untuk kita. supaya boleh guna async dan await