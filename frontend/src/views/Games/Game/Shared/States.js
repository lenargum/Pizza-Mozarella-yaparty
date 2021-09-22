const States = {
  Player: {
    STARTING: "p_starting",
    READY: "p_ready",
    ANSWERING: "p_answering",
    ANSWERED: "p_answered",
    WAITING: "p_waiting",
    WAITED: "p_waited"
  },
  Judge: {
    STARTING: "j_starting",
    READY: "j_ready",
    ANSWERING: "j_answering",
    CHECKING: "j_checking",
    ANSWERED: "j_answered",
    CONTINUE: "j_continue",
  },
  Game: {
    CREATE: "create",
    LOGIN: "login",
    ROLE: "role",
    PLAYING: "playing",
    SCOREBOARD: "scoreboard"
  }
};
export default States;