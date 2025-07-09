/*************** 
 * Stroop *
 ***************/


// store info about the experiment session:
let expName = 'stroop';  // from the Builder filename that created this script
let expInfo = {
    'participant': `${util.pad(Number.parseFloat(util.randint(0, 999999)).toFixed(0), 6)}`,
    'session': '001',
};

// Start code blocks for 'Before Experiment'
// init psychoJS:
const psychoJS = new PsychoJS({
  debug: true
});

// open window:
psychoJS.openWindow({
  fullscr: true,
  color: new util.Color([0,0,0]),
  units: 'height',
  waitBlanking: true,
  backgroundImage: '',
  backgroundFit: 'none',
});
// schedule the experiment:
psychoJS.schedule(psychoJS.gui.DlgFromDict({
  dictionary: expInfo,
  title: expName
}));

const flowScheduler = new Scheduler(psychoJS);
const dialogCancelScheduler = new Scheduler(psychoJS);
psychoJS.scheduleCondition(function() { return (psychoJS.gui.dialogComponent.button === 'OK'); },flowScheduler, dialogCancelScheduler);

// flowScheduler gets run if the participants presses OK
flowScheduler.add(updateInfo); // add timeStamp
flowScheduler.add(experimentInit);
flowScheduler.add(instrucciones_generalesRoutineBegin());
flowScheduler.add(instrucciones_generalesRoutineEachFrame());
flowScheduler.add(instrucciones_generalesRoutineEnd());
flowScheduler.add(instrucciones_especificasRoutineBegin());
flowScheduler.add(instrucciones_especificasRoutineEachFrame());
flowScheduler.add(instrucciones_especificasRoutineEnd());
flowScheduler.add(ITI_inicialRoutineBegin());
flowScheduler.add(ITI_inicialRoutineEachFrame());
flowScheduler.add(ITI_inicialRoutineEnd());
const practica_cLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(practica_cLoopBegin(practica_cLoopScheduler));
flowScheduler.add(practica_cLoopScheduler);
flowScheduler.add(practica_cLoopEnd);




flowScheduler.add(instrucciones_especificasRoutineBegin());
flowScheduler.add(instrucciones_especificasRoutineEachFrame());
flowScheduler.add(instrucciones_especificasRoutineEnd());
flowScheduler.add(ITI_inicialRoutineBegin());
flowScheduler.add(ITI_inicialRoutineEachFrame());
flowScheduler.add(ITI_inicialRoutineEnd());
const trialsLoopScheduler = new Scheduler(psychoJS);
flowScheduler.add(trialsLoopBegin(trialsLoopScheduler));
flowScheduler.add(trialsLoopScheduler);
flowScheduler.add(trialsLoopEnd);


flowScheduler.add(instrucciones_especificasRoutineBegin());
flowScheduler.add(instrucciones_especificasRoutineEachFrame());
flowScheduler.add(instrucciones_especificasRoutineEnd());
flowScheduler.add(quitPsychoJS, 'Thank you for your patience.', true);

// quit if user presses Cancel in dialog box:
dialogCancelScheduler.add(quitPsychoJS, 'Thank you for your patience.', false);

psychoJS.start({
  expName: expName,
  expInfo: expInfo,
  resources: [
    // resources:
    {'name': 'conditions/practica_C.csv', 'path': 'conditions/practica_C.csv'},
    {'name': 'conditions/practica_C.csv', 'path': 'conditions/practica_C.csv'},
  ]
});

psychoJS.experimentLogger.setLevel(core.Logger.ServerLevel.INFO);


var currentLoop;
var frameDur;
async function updateInfo() {
  currentLoop = psychoJS.experiment;  // right now there are no loops
  expInfo['date'] = util.MonotonicClock.getDateStr();  // add a simple timestamp
  expInfo['expName'] = expName;
  expInfo['psychopyVersion'] = '2024.2.4';
  expInfo['OS'] = window.navigator.platform;


  // store frame rate of monitor if we can measure it successfully
  expInfo['frameRate'] = psychoJS.window.getActualFrameRate();
  if (typeof expInfo['frameRate'] !== 'undefined')
    frameDur = 1.0 / Math.round(expInfo['frameRate']);
  else
    frameDur = 1.0 / 60.0; // couldn't get a reliable measure so guess

  // add info from the URL:
  util.addInfoFromUrl(expInfo);
  

  
  psychoJS.experiment.dataFileName = (("." + "/") + `data/${expInfo["participant"]}_${expName}_${expInfo["date"]}`);
  psychoJS.experiment.field_separator = ',';


  return Scheduler.Event.NEXT;
}


var instrucciones_generalesClock;
var texto_instrucciones;
var key_next;
var instrucciones_especificasClock;
var texto_instrucciones_c;
var key_next_c;
var ITI_inicialClock;
var cruz;
var ensayo_practica_cClock;
var texto_estimulo_ensayo_C;
var respuesta_teclado_ensayo_C;
var CRUZ_ensayo_C;
var frameClock;
var text;
var feedback_practicaClock;
var feedback_text;
var condicion_cClock;
var texto_estimulo_C;
var respuesta_teclado_C;
var CRUZ_C;
var globalClock;
var routineTimer;
async function experimentInit() {
  // Initialize components for Routine "instrucciones_generales"
  instrucciones_generalesClock = new util.Clock();
  texto_instrucciones = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto_instrucciones',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], draggable: false, height: 0.04,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  key_next = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "instrucciones_especificas"
  instrucciones_especificasClock = new util.Clock();
  texto_instrucciones_c = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto_instrucciones_c',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, (- 0.05)], draggable: false, height: 0.05,  wrapWidth: 1.5, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  key_next_c = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  // Initialize components for Routine "ITI_inicial"
  ITI_inicialClock = new util.Clock();
  cruz = new visual.ShapeStim ({
    win: psychoJS.window, name: 'cruz', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: 0, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "ensayo_practica_c"
  ensayo_practica_cClock = new util.Clock();
  texto_estimulo_ensayo_C = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto_estimulo_ensayo_C',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], draggable: false, height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  respuesta_teclado_ensayo_C = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  CRUZ_ensayo_C = new visual.ShapeStim ({
    win: psychoJS.window, name: 'CRUZ_ensayo_C', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  // Initialize components for Routine "frame"
  frameClock = new util.Clock();
  text = new visual.TextStim({
    win: psychoJS.window,
    name: 'text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.05,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "feedback_practica"
  feedback_practicaClock = new util.Clock();
  feedback_text = new visual.TextStim({
    win: psychoJS.window,
    name: 'feedback_text',
    text: '',
    font: 'Arial',
    units: undefined, 
    pos: [0, 0], draggable: false, height: 0.1,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color(undefined),  opacity: undefined,
    depth: 0.0 
  });
  
  // Initialize components for Routine "condicion_c"
  condicion_cClock = new util.Clock();
  texto_estimulo_C = new visual.TextStim({
    win: psychoJS.window,
    name: 'texto_estimulo_C',
    text: '',
    font: 'Arial',
    units: 'height', 
    pos: [0, 0], draggable: false, height: 0.09,  wrapWidth: undefined, ori: 0.0,
    languageStyle: 'LTR',
    color: new util.Color('white'),  opacity: 1.0,
    depth: 0.0 
  });
  
  respuesta_teclado_C = new core.Keyboard({psychoJS: psychoJS, clock: new util.Clock(), waitForStart: true});
  
  CRUZ_C = new visual.ShapeStim ({
    win: psychoJS.window, name: 'CRUZ_C', 
    vertices: 'cross', size:[0.1, 0.1],
    ori: 0.0, 
    pos: [0, 0], 
    draggable: false, 
    anchor: 'center', 
    lineWidth: 1.0, 
    lineColor: new util.Color('white'), 
    fillColor: new util.Color('white'), 
    colorSpace: 'rgb', 
    opacity: undefined, 
    depth: -2, 
    interpolate: true, 
  });
  
  // Create some handy timers
  globalClock = new util.Clock();  // to track the time since experiment started
  routineTimer = new util.CountdownTimer();  // to track time remaining of each (non-slip) routine
  
  return Scheduler.Event.NEXT;
}


var t;
var frameN;
var continueRoutine;
var instrucciones_generalesMaxDurationReached;
var _key_next_allKeys;
var instrucciones_generalesMaxDuration;
var instrucciones_generalesComponents;
function instrucciones_generalesRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instrucciones_generales' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instrucciones_generalesClock.reset();
    routineTimer.reset();
    instrucciones_generalesMaxDurationReached = false;
    // update component parameters for each repeat
    texto_instrucciones.setText('Durante esta tarea, verás palabras o cadenas de letras presentadas en distintos colores.\nTu tarea es indicar el color de la tinta, ignorando el significado de la palabra.\n\nResponde usando las siguientes teclas:\n↑  para ROJO  \n↓  para AZUL  \n←  para VERDE  \n→  para AMARILLO\n\nHabrá una leyenda visible en pantalla que te recordará estas asociaciones.\n\nIntenta responder lo más rápido y correctamente posible.\nSi no respondes dentro de 2500 ms, se contará como omisión.\n\nPresiona espacio para ir al bloque de practica.\n');
    key_next.keys = undefined;
    key_next.rt = undefined;
    _key_next_allKeys = [];
    psychoJS.experiment.addData('instrucciones_generales.started', globalClock.getTime());
    instrucciones_generalesMaxDuration = null
    // keep track of which components have finished
    instrucciones_generalesComponents = [];
    instrucciones_generalesComponents.push(texto_instrucciones);
    instrucciones_generalesComponents.push(key_next);
    
    instrucciones_generalesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrucciones_generalesRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instrucciones_generales' ---
    // get current time
    t = instrucciones_generalesClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *texto_instrucciones* updates
    if (t >= 0.0 && texto_instrucciones.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto_instrucciones.tStart = t;  // (not accounting for frame time here)
      texto_instrucciones.frameNStart = frameN;  // exact frame index
      
      texto_instrucciones.setAutoDraw(true);
    }
    
    
    // *key_next* updates
    if (t >= 0.0 && key_next.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_next.tStart = t;  // (not accounting for frame time here)
      key_next.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_next.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_next.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_next.clearEvents(); });
    }
    
    if (key_next.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_next.getKeys({keyList: ['space'], waitRelease: false});
      _key_next_allKeys = _key_next_allKeys.concat(theseKeys);
      if (_key_next_allKeys.length > 0) {
        key_next.keys = _key_next_allKeys[_key_next_allKeys.length - 1].name;  // just the last key pressed
        key_next.rt = _key_next_allKeys[_key_next_allKeys.length - 1].rt;
        key_next.duration = _key_next_allKeys[_key_next_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrucciones_generalesComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrucciones_generalesRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instrucciones_generales' ---
    instrucciones_generalesComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instrucciones_generales.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_next.corr, level);
    }
    psychoJS.experiment.addData('key_next.keys', key_next.keys);
    if (typeof key_next.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_next.rt', key_next.rt);
        psychoJS.experiment.addData('key_next.duration', key_next.duration);
        routineTimer.reset();
        }
    
    key_next.stop();
    // the Routine "instrucciones_generales" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var instrucciones_especificasMaxDurationReached;
var _key_next_c_allKeys;
var instrucciones_especificasMaxDuration;
var instrucciones_especificasComponents;
function instrucciones_especificasRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'instrucciones_especificas' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    instrucciones_especificasClock.reset();
    routineTimer.reset();
    instrucciones_especificasMaxDurationReached = false;
    // update component parameters for each repeat
    texto_instrucciones_c.setText('En este bloque verás figuras como “XXXX” presentadas en diferentes colores.  \nTu tarea es indicar el color de la tinta lo más rápido y correctamente posible.\n\nUsa las siguientes teclas:\n↑ = ROJO   ↓ = AZUL   ← = VERDE   → = AMARILLO\n\nRecuerda que la leyenda estará visible durante toda la tarea.\n\nPresiona la barra espaciadora para comenzar.');
    key_next_c.keys = undefined;
    key_next_c.rt = undefined;
    _key_next_c_allKeys = [];
    psychoJS.experiment.addData('instrucciones_especificas.started', globalClock.getTime());
    instrucciones_especificasMaxDuration = null
    // keep track of which components have finished
    instrucciones_especificasComponents = [];
    instrucciones_especificasComponents.push(texto_instrucciones_c);
    instrucciones_especificasComponents.push(key_next_c);
    
    instrucciones_especificasComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function instrucciones_especificasRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'instrucciones_especificas' ---
    // get current time
    t = instrucciones_especificasClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *texto_instrucciones_c* updates
    if (t >= 0.0 && texto_instrucciones_c.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto_instrucciones_c.tStart = t;  // (not accounting for frame time here)
      texto_instrucciones_c.frameNStart = frameN;  // exact frame index
      
      texto_instrucciones_c.setAutoDraw(true);
    }
    
    
    // *key_next_c* updates
    if (t >= 0.0 && key_next_c.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      key_next_c.tStart = t;  // (not accounting for frame time here)
      key_next_c.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { key_next_c.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { key_next_c.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { key_next_c.clearEvents(); });
    }
    
    if (key_next_c.status === PsychoJS.Status.STARTED) {
      let theseKeys = key_next_c.getKeys({keyList: ['space'], waitRelease: false});
      _key_next_c_allKeys = _key_next_c_allKeys.concat(theseKeys);
      if (_key_next_c_allKeys.length > 0) {
        key_next_c.keys = _key_next_c_allKeys[_key_next_c_allKeys.length - 1].name;  // just the last key pressed
        key_next_c.rt = _key_next_c_allKeys[_key_next_c_allKeys.length - 1].rt;
        key_next_c.duration = _key_next_c_allKeys[_key_next_c_allKeys.length - 1].duration;
        // a response ends the routine
        continueRoutine = false;
      }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    instrucciones_especificasComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function instrucciones_especificasRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'instrucciones_especificas' ---
    instrucciones_especificasComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('instrucciones_especificas.stopped', globalClock.getTime());
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(key_next_c.corr, level);
    }
    psychoJS.experiment.addData('key_next_c.keys', key_next_c.keys);
    if (typeof key_next_c.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('key_next_c.rt', key_next_c.rt);
        psychoJS.experiment.addData('key_next_c.duration', key_next_c.duration);
        routineTimer.reset();
        }
    
    key_next_c.stop();
    // the Routine "instrucciones_especificas" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var ITI_inicialMaxDurationReached;
var ITI_inicialMaxDuration;
var ITI_inicialComponents;
function ITI_inicialRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ITI_inicial' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ITI_inicialClock.reset(routineTimer.getTime());
    routineTimer.add(0.500000);
    ITI_inicialMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('ITI_inicial.started', globalClock.getTime());
    ITI_inicialMaxDuration = null
    // keep track of which components have finished
    ITI_inicialComponents = [];
    ITI_inicialComponents.push(cruz);
    
    ITI_inicialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var frameRemains;
function ITI_inicialRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ITI_inicial' ---
    // get current time
    t = ITI_inicialClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *cruz* updates
    if (t >= 0.0 && cruz.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      cruz.tStart = t;  // (not accounting for frame time here)
      cruz.frameNStart = frameN;  // exact frame index
      
      cruz.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (cruz.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      cruz.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ITI_inicialComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function ITI_inicialRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ITI_inicial' ---
    ITI_inicialComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ITI_inicial.stopped', globalClock.getTime());
    if (ITI_inicialMaxDurationReached) {
        ITI_inicialClock.add(ITI_inicialMaxDuration);
    } else {
        ITI_inicialClock.add(0.500000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var practica_c;
function practica_cLoopBegin(practica_cLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    practica_c = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 1, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/practica_C.csv',
      seed: undefined, name: 'practica_c'
    });
    psychoJS.experiment.addLoop(practica_c); // add the loop to the experiment
    currentLoop = practica_c;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    practica_c.forEach(function() {
      snapshot = practica_c.getSnapshot();
    
      practica_cLoopScheduler.add(importConditions(snapshot));
      practica_cLoopScheduler.add(ensayo_practica_cRoutineBegin(snapshot));
      practica_cLoopScheduler.add(ensayo_practica_cRoutineEachFrame());
      practica_cLoopScheduler.add(ensayo_practica_cRoutineEnd(snapshot));
      practica_cLoopScheduler.add(frameRoutineBegin(snapshot));
      practica_cLoopScheduler.add(frameRoutineEachFrame());
      practica_cLoopScheduler.add(frameRoutineEnd(snapshot));
      practica_cLoopScheduler.add(feedback_practicaRoutineBegin(snapshot));
      practica_cLoopScheduler.add(feedback_practicaRoutineEachFrame());
      practica_cLoopScheduler.add(feedback_practicaRoutineEnd(snapshot));
      practica_cLoopScheduler.add(practica_cLoopEndIteration(practica_cLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function practica_cLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(practica_c);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function practica_cLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var trials;
function trialsLoopBegin(trialsLoopScheduler, snapshot) {
  return async function() {
    TrialHandler.fromSnapshot(snapshot); // update internal variables (.thisN etc) of the loop
    
    // set up handler to look after randomisation of conditions etc
    trials = new TrialHandler({
      psychoJS: psychoJS,
      nReps: 9, method: TrialHandler.Method.RANDOM,
      extraInfo: expInfo, originPath: undefined,
      trialList: 'conditions/practica_C.csv',
      seed: undefined, name: 'trials'
    });
    psychoJS.experiment.addLoop(trials); // add the loop to the experiment
    currentLoop = trials;  // we're now the current loop
    
    // Schedule all the trials in the trialList:
    trials.forEach(function() {
      snapshot = trials.getSnapshot();
    
      trialsLoopScheduler.add(importConditions(snapshot));
      trialsLoopScheduler.add(condicion_cRoutineBegin(snapshot));
      trialsLoopScheduler.add(condicion_cRoutineEachFrame());
      trialsLoopScheduler.add(condicion_cRoutineEnd(snapshot));
      trialsLoopScheduler.add(trialsLoopEndIteration(trialsLoopScheduler, snapshot));
    });
    
    return Scheduler.Event.NEXT;
  }
}


async function trialsLoopEnd() {
  // terminate loop
  psychoJS.experiment.removeLoop(trials);
  // update the current loop from the ExperimentHandler
  if (psychoJS.experiment._unfinishedLoops.length>0)
    currentLoop = psychoJS.experiment._unfinishedLoops.at(-1);
  else
    currentLoop = psychoJS.experiment;  // so we use addData from the experiment
  return Scheduler.Event.NEXT;
}


function trialsLoopEndIteration(scheduler, snapshot) {
  // ------Prepare for next entry------
  return async function () {
    if (typeof snapshot !== 'undefined') {
      // ------Check if user ended loop early------
      if (snapshot.finished) {
        // Check for and save orphaned data
        if (psychoJS.experiment.isEntryEmpty()) {
          psychoJS.experiment.nextEntry(snapshot);
        }
        scheduler.stop();
      } else {
        psychoJS.experiment.nextEntry(snapshot);
      }
    return Scheduler.Event.NEXT;
    }
  };
}


var ensayo_practica_cMaxDurationReached;
var _respuesta_teclado_ensayo_C_allKeys;
var respuesta_registrada;
var tiempo_respuesta;
var inicio_ensayo;
var ensayo_practica_cMaxDuration;
var ensayo_practica_cComponents;
function ensayo_practica_cRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'ensayo_practica_c' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    ensayo_practica_cClock.reset();
    routineTimer.reset();
    ensayo_practica_cMaxDurationReached = false;
    // update component parameters for each repeat
    texto_estimulo_ensayo_C.setColor(new util.Color(color_tinta));
    texto_estimulo_ensayo_C.setText(palabra);
    respuesta_teclado_ensayo_C.keys = undefined;
    respuesta_teclado_ensayo_C.rt = undefined;
    _respuesta_teclado_ensayo_C_allKeys = [];
    // Run 'Begin Routine' code from Code_ensayo_C
    respuesta_registrada = false;
    tiempo_respuesta = null;
    inicio_ensayo = globalClock.getTime();
    texto_estimulo_ensayo_C.setAutoDraw(true);
    CRUZ_ensayo_C.setAutoDraw(false);
    
    psychoJS.experiment.addData('ensayo_practica_c.started', globalClock.getTime());
    ensayo_practica_cMaxDuration = null
    // keep track of which components have finished
    ensayo_practica_cComponents = [];
    ensayo_practica_cComponents.push(texto_estimulo_ensayo_C);
    ensayo_practica_cComponents.push(respuesta_teclado_ensayo_C);
    ensayo_practica_cComponents.push(CRUZ_ensayo_C);
    
    ensayo_practica_cComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


var tiempo_actual;
function ensayo_practica_cRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'ensayo_practica_c' ---
    // get current time
    t = ensayo_practica_cClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *texto_estimulo_ensayo_C* updates
    if (t >= 0.0 && texto_estimulo_ensayo_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto_estimulo_ensayo_C.tStart = t;  // (not accounting for frame time here)
      texto_estimulo_ensayo_C.frameNStart = frameN;  // exact frame index
      
      texto_estimulo_ensayo_C.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (texto_estimulo_ensayo_C.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      texto_estimulo_ensayo_C.setAutoDraw(false);
    }
    
    
    // *respuesta_teclado_ensayo_C* updates
    if (t >= 0.0 && respuesta_teclado_ensayo_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respuesta_teclado_ensayo_C.tStart = t;  // (not accounting for frame time here)
      respuesta_teclado_ensayo_C.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respuesta_teclado_ensayo_C.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respuesta_teclado_ensayo_C.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respuesta_teclado_ensayo_C.clearEvents(); });
    }
    
    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (respuesta_teclado_ensayo_C.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      respuesta_teclado_ensayo_C.status = PsychoJS.Status.FINISHED;
        }
      
    if (respuesta_teclado_ensayo_C.status === PsychoJS.Status.STARTED) {
      let theseKeys = respuesta_teclado_ensayo_C.getKeys({keyList: ['up', 'down', 'left', 'right'], waitRelease: false});
      _respuesta_teclado_ensayo_C_allKeys = _respuesta_teclado_ensayo_C_allKeys.concat(theseKeys);
      if (_respuesta_teclado_ensayo_C_allKeys.length > 0) {
        respuesta_teclado_ensayo_C.keys = _respuesta_teclado_ensayo_C_allKeys[_respuesta_teclado_ensayo_C_allKeys.length - 1].name;  // just the last key pressed
        respuesta_teclado_ensayo_C.rt = _respuesta_teclado_ensayo_C_allKeys[_respuesta_teclado_ensayo_C_allKeys.length - 1].rt;
        respuesta_teclado_ensayo_C.duration = _respuesta_teclado_ensayo_C_allKeys[_respuesta_teclado_ensayo_C_allKeys.length - 1].duration;
        // was this correct?
        if (respuesta_teclado_ensayo_C.keys == tecla_correcta) {
            respuesta_teclado_ensayo_C.corr = 1;
        } else {
            respuesta_teclado_ensayo_C.corr = 0;
        }
      }
    }
    
    
    // *CRUZ_ensayo_C* updates
    if ((false) && CRUZ_ensayo_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CRUZ_ensayo_C.tStart = t;  // (not accounting for frame time here)
      CRUZ_ensayo_C.frameNStart = frameN;  // exact frame index
      
      CRUZ_ensayo_C.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from Code_ensayo_C
    tiempo_actual = (globalClock.getTime() - inicio_ensayo);
    if ((respuesta_teclado_ensayo_C.keys && (! respuesta_registrada))) {
        respuesta_registrada = true;
        tiempo_respuesta = tiempo_actual;
        texto_estimulo_ensayo_C.setAutoDraw(false);
        CRUZ_ensayo_C.setAutoDraw(true);
        respuesta_teclado_ensayo_C.status = PsychoJS.Status.FINISHED;
    } else {
        if (((tiempo_actual >= 2.5) && (! respuesta_registrada))) {
            respuesta_registrada = true;
            texto_estimulo_ensayo_C.setAutoDraw(false);
            CRUZ_ensayo_C.setAutoDraw(true);
            respuesta_teclado_ensayo_C.status = PsychoJS.Status.FINISHED;
        } else {
            if ((tiempo_actual >= 3.0)) {
                continueRoutine = false;
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    ensayo_practica_cComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


var validez;
function ensayo_practica_cRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'ensayo_practica_c' ---
    ensayo_practica_cComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('ensayo_practica_c.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (respuesta_teclado_ensayo_C.keys === undefined) {
      if (['None','none',undefined].includes(tecla_correcta)) {
         respuesta_teclado_ensayo_C.corr = 1;  // correct non-response
      } else {
         respuesta_teclado_ensayo_C.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respuesta_teclado_ensayo_C.corr, level);
    }
    psychoJS.experiment.addData('respuesta_teclado_ensayo_C.keys', respuesta_teclado_ensayo_C.keys);
    psychoJS.experiment.addData('respuesta_teclado_ensayo_C.corr', respuesta_teclado_ensayo_C.corr);
    if (typeof respuesta_teclado_ensayo_C.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respuesta_teclado_ensayo_C.rt', respuesta_teclado_ensayo_C.rt);
        psychoJS.experiment.addData('respuesta_teclado_ensayo_C.duration', respuesta_teclado_ensayo_C.duration);
        }
    
    respuesta_teclado_ensayo_C.stop();
    // Run 'End Routine' code from Code_ensayo_C
    if (tiempo_respuesta) {
        if ((tiempo_respuesta < 0.2)) {
            validez = "anticipada";
            respuesta_teclado_ensayo_C.corr = 0;
        } else {
            validez = "valida";
        }
    } else {
        validez = "omitida";
    }
    psychoJS.experiment.addData("validez", validez);
    CRUZ_ensayo_C.setAutoDraw(false);
    psychoJS.experiment.addData("RT", (tiempo_respuesta ? tiempo_respuesta : "NA"));
    psychoJS.experiment.addData("key", respuesta_teclado_ensayo_C.keys);
    try {
        feedback_corr = Number.parseInt(respuesta_teclado_ensayoC.corr);
    } catch(e) {
        feedback_corr = 0;
    }
    
    // the Routine "ensayo_practica_c" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var frameMaxDurationReached;
var frameMaxDuration;
var frameComponents;
function frameRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'frame' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    frameClock.reset(routineTimer.getTime());
    routineTimer.add(0.000100);
    frameMaxDurationReached = false;
    // update component parameters for each repeat
    psychoJS.experiment.addData('frame.started', globalClock.getTime());
    frameMaxDuration = null
    // keep track of which components have finished
    frameComponents = [];
    frameComponents.push(text);
    
    frameComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function frameRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'frame' ---
    // get current time
    t = frameClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *text* updates
    if (t >= 0.0 && text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      text.tStart = t;  // (not accounting for frame time here)
      text.frameNStart = frameN;  // exact frame index
      
      text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 0.0001 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    frameComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function frameRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'frame' ---
    frameComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('frame.stopped', globalClock.getTime());
    if (frameMaxDurationReached) {
        frameClock.add(frameMaxDuration);
    } else {
        frameClock.add(0.000100);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var feedback_practicaMaxDurationReached;
var feedback_practicaMaxDuration;
var feedback_practicaComponents;
function feedback_practicaRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'feedback_practica' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    feedback_practicaClock.reset(routineTimer.getTime());
    routineTimer.add(1.000000);
    feedback_practicaMaxDurationReached = false;
    // update component parameters for each repeat
    feedback_text.setText('\n');
    // Run 'Begin Routine' code from codigo_feedback
    if ((feedback_corr === 1)) {
        feedback_text.text = "\u2714";
        feedback_text.color = "green";
    } else {
        feedback_text.text = "\u2716";
        feedback_text.color = "red";
    }
    
    psychoJS.experiment.addData('feedback_practica.started', globalClock.getTime());
    feedback_practicaMaxDuration = null
    // keep track of which components have finished
    feedback_practicaComponents = [];
    feedback_practicaComponents.push(feedback_text);
    
    feedback_practicaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function feedback_practicaRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'feedback_practica' ---
    // get current time
    t = feedback_practicaClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *feedback_text* updates
    if (t >= 0.0 && feedback_text.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      feedback_text.tStart = t;  // (not accounting for frame time here)
      feedback_text.frameNStart = frameN;  // exact frame index
      
      feedback_text.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 1.0 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (feedback_text.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      feedback_text.setAutoDraw(false);
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    feedback_practicaComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine && routineTimer.getTime() > 0) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function feedback_practicaRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'feedback_practica' ---
    feedback_practicaComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('feedback_practica.stopped', globalClock.getTime());
    // Run 'End Routine' code from codigo_feedback
    feedback_text.setAutoDraw(false);
    
    if (feedback_practicaMaxDurationReached) {
        feedback_practicaClock.add(feedback_practicaMaxDuration);
    } else {
        feedback_practicaClock.add(1.000000);
    }
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


var condicion_cMaxDurationReached;
var _respuesta_teclado_C_allKeys;
var condicion_cMaxDuration;
var condicion_cComponents;
function condicion_cRoutineBegin(snapshot) {
  return async function () {
    TrialHandler.fromSnapshot(snapshot); // ensure that .thisN vals are up to date
    
    //--- Prepare to start Routine 'condicion_c' ---
    t = 0;
    frameN = -1;
    continueRoutine = true; // until we're told otherwise
    condicion_cClock.reset();
    routineTimer.reset();
    condicion_cMaxDurationReached = false;
    // update component parameters for each repeat
    texto_estimulo_C.setColor(new util.Color(color_tinta));
    texto_estimulo_C.setText(palabra);
    respuesta_teclado_C.keys = undefined;
    respuesta_teclado_C.rt = undefined;
    _respuesta_teclado_C_allKeys = [];
    // Run 'Begin Routine' code from Code_C
    respuesta_registrada = false;
    tiempo_respuesta = null;
    inicio_ensayo = globalClock.getTime();
    texto_estimulo_C.setAutoDraw(true);
    CRUZ_C.setAutoDraw(false);
    
    psychoJS.experiment.addData('condicion_c.started', globalClock.getTime());
    condicion_cMaxDuration = null
    // keep track of which components have finished
    condicion_cComponents = [];
    condicion_cComponents.push(texto_estimulo_C);
    condicion_cComponents.push(respuesta_teclado_C);
    condicion_cComponents.push(CRUZ_C);
    
    condicion_cComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent)
        thisComponent.status = PsychoJS.Status.NOT_STARTED;
       });
    return Scheduler.Event.NEXT;
  }
}


function condicion_cRoutineEachFrame() {
  return async function () {
    //--- Loop for each frame of Routine 'condicion_c' ---
    // get current time
    t = condicion_cClock.getTime();
    frameN = frameN + 1;// number of completed frames (so 0 is the first frame)
    // update/draw components on each frame
    
    // *texto_estimulo_C* updates
    if (t >= 0.0 && texto_estimulo_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      texto_estimulo_C.tStart = t;  // (not accounting for frame time here)
      texto_estimulo_C.frameNStart = frameN;  // exact frame index
      
      texto_estimulo_C.setAutoDraw(true);
    }
    
    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (texto_estimulo_C.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      texto_estimulo_C.setAutoDraw(false);
    }
    
    
    // *respuesta_teclado_C* updates
    if (t >= 0.0 && respuesta_teclado_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      respuesta_teclado_C.tStart = t;  // (not accounting for frame time here)
      respuesta_teclado_C.frameNStart = frameN;  // exact frame index
      
      // keyboard checking is just starting
      psychoJS.window.callOnFlip(function() { respuesta_teclado_C.clock.reset(); });  // t=0 on next screen flip
      psychoJS.window.callOnFlip(function() { respuesta_teclado_C.start(); }); // start on screen flip
      psychoJS.window.callOnFlip(function() { respuesta_teclado_C.clearEvents(); });
    }
    
    frameRemains = 0.0 + 2.5 - psychoJS.window.monitorFramePeriod * 0.75;// most of one frame period left
    if (respuesta_teclado_C.status === PsychoJS.Status.STARTED && t >= frameRemains) {
      respuesta_teclado_C.status = PsychoJS.Status.FINISHED;
        }
      
    if (respuesta_teclado_C.status === PsychoJS.Status.STARTED) {
      let theseKeys = respuesta_teclado_C.getKeys({keyList: ['up', 'down', 'left', 'right'], waitRelease: false});
      _respuesta_teclado_C_allKeys = _respuesta_teclado_C_allKeys.concat(theseKeys);
      if (_respuesta_teclado_C_allKeys.length > 0) {
        respuesta_teclado_C.keys = _respuesta_teclado_C_allKeys[_respuesta_teclado_C_allKeys.length - 1].name;  // just the last key pressed
        respuesta_teclado_C.rt = _respuesta_teclado_C_allKeys[_respuesta_teclado_C_allKeys.length - 1].rt;
        respuesta_teclado_C.duration = _respuesta_teclado_C_allKeys[_respuesta_teclado_C_allKeys.length - 1].duration;
        // was this correct?
        if (respuesta_teclado_C.keys == tecla_correcta) {
            respuesta_teclado_C.corr = 1;
        } else {
            respuesta_teclado_C.corr = 0;
        }
      }
    }
    
    
    // *CRUZ_C* updates
    if ((false) && CRUZ_C.status === PsychoJS.Status.NOT_STARTED) {
      // keep track of start time/frame for later
      CRUZ_C.tStart = t;  // (not accounting for frame time here)
      CRUZ_C.frameNStart = frameN;  // exact frame index
      
      CRUZ_C.setAutoDraw(true);
    }
    
    // Run 'Each Frame' code from Code_C
    tiempo_actual = (globalClock.getTime() - inicio_ensayo);
    if ((respuesta_teclado_C.keys && (! respuesta_registrada))) {
        respuesta_registrada = true;
        tiempo_respuesta = tiempo_actual;
        texto_estimulo_C.setAutoDraw(false);
        CRUZ_C.setAutoDraw(true);
        respuesta_teclado_C.status = PsychoJS.Status.FINISHED;
    } else {
        if (((tiempo_actual >= 2.5) && (! respuesta_registrada))) {
            respuesta_registrada = true;
            texto_estimulo_C.setAutoDraw(false);
            CRUZ_C.setAutoDraw(true);
            respuesta_teclado_C.status = PsychoJS.Status.FINISHED;
        } else {
            if ((tiempo_actual >= 3.0)) {
                continueRoutine = false;
            }
        }
    }
    
    // check for quit (typically the Esc key)
    if (psychoJS.experiment.experimentEnded || psychoJS.eventManager.getKeys({keyList:['escape']}).length > 0) {
      return quitPsychoJS('The [Escape] key was pressed. Goodbye!', false);
    }
    
    // check if the Routine should terminate
    if (!continueRoutine) {  // a component has requested a forced-end of Routine
      return Scheduler.Event.NEXT;
    }
    
    continueRoutine = false;  // reverts to True if at least one component still running
    condicion_cComponents.forEach( function(thisComponent) {
      if ('status' in thisComponent && thisComponent.status !== PsychoJS.Status.FINISHED) {
        continueRoutine = true;
      }
    });
    
    // refresh the screen if continuing
    if (continueRoutine) {
      return Scheduler.Event.FLIP_REPEAT;
    } else {
      return Scheduler.Event.NEXT;
    }
  };
}


function condicion_cRoutineEnd(snapshot) {
  return async function () {
    //--- Ending Routine 'condicion_c' ---
    condicion_cComponents.forEach( function(thisComponent) {
      if (typeof thisComponent.setAutoDraw === 'function') {
        thisComponent.setAutoDraw(false);
      }
    });
    psychoJS.experiment.addData('condicion_c.stopped', globalClock.getTime());
    // was no response the correct answer?!
    if (respuesta_teclado_C.keys === undefined) {
      if (['None','none',undefined].includes(tecla_correcta)) {
         respuesta_teclado_C.corr = 1;  // correct non-response
      } else {
         respuesta_teclado_C.corr = 0;  // failed to respond (incorrectly)
      }
    }
    // store data for current loop
    // update the trial handler
    if (currentLoop instanceof MultiStairHandler) {
      currentLoop.addResponse(respuesta_teclado_C.corr, level);
    }
    psychoJS.experiment.addData('respuesta_teclado_C.keys', respuesta_teclado_C.keys);
    psychoJS.experiment.addData('respuesta_teclado_C.corr', respuesta_teclado_C.corr);
    if (typeof respuesta_teclado_C.keys !== 'undefined') {  // we had a response
        psychoJS.experiment.addData('respuesta_teclado_C.rt', respuesta_teclado_C.rt);
        psychoJS.experiment.addData('respuesta_teclado_C.duration', respuesta_teclado_C.duration);
        }
    
    respuesta_teclado_C.stop();
    // Run 'End Routine' code from Code_C
    if (tiempo_respuesta) {
        if ((tiempo_respuesta < 0.2)) {
            validez = "anticipada";
            respuesta_teclado_C.corr = 0;
        } else {
            validez = "valida";
        }
    } else {
        validez = "omitida";
    }
    psychoJS.experiment.addData("validez", validez);
    CRUZ_C.setAutoDraw(false);
    psychoJS.experiment.addData("RT", (tiempo_respuesta ? tiempo_respuesta : "NA"));
    psychoJS.experiment.addData("key", respuesta_teclado_C.keys);
    
    // the Routine "condicion_c" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset();
    
    // Routines running outside a loop should always advance the datafile row
    if (currentLoop === psychoJS.experiment) {
      psychoJS.experiment.nextEntry(snapshot);
    }
    return Scheduler.Event.NEXT;
  }
}


function importConditions(currentLoop) {
  return async function () {
    psychoJS.importAttributes(currentLoop.getCurrentTrial());
    return Scheduler.Event.NEXT;
    };
}


async function quitPsychoJS(message, isCompleted) {
  // Check for and save orphaned data
  if (psychoJS.experiment.isEntryEmpty()) {
    psychoJS.experiment.nextEntry();
  }
  psychoJS.window.close();
  psychoJS.quit({message: message, isCompleted: isCompleted});
  
  return Scheduler.Event.QUIT;
}
