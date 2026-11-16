from enum import IntFlag

# ==============================================================================
# 1. ALU, LOGIC & EXECUTION REGISTERS (8-BIT BYTE BINDINGS)
# ==============================================================================

class Operators(IntFlag):
    NONE     = 0
    LESSER   = 1 << 0
    BIGGER   = 1 << 1
    MIN      = 1 << 2
    MAX      = 1 << 3
    IN       = 1 << 4
    OUT      = 1 << 5
    INCLUDES = 1 << 6
    EXCLUDES = 1 << 7

class Compares(IntFlag):
    NONE      = 0
    EQUAL     = 1 << 0
    APART     = 1 << 1
    SIMILAR   = 1 << 2
    DIFFERENT = 1 << 3
    EVER      = 1 << 4
    NEVER     = 1 << 5

class Shifts(IntFlag):
    NONE   = 0
    OR     = 1 << 0
    AND    = 1 << 1
    IS     = 1 << 2
    NOT    = 1 << 3
    XOR    = 1 << 4
    INVERT = 1 << 5
    SHL    = 1 << 6
    SHR    = 1 << 7

class Arithmics(IntFlag):
    NONE     = 0
    ADD      = 1 << 0
    INC      = 1 << 1
    SUB      = 1 << 2
    DEC      = 1 << 3
    UP       = 1 << 4
    DOWN     = 1 << 5
    MULTIPLY = 1 << 6
    DIVIDE   = 1 << 7

class Evaluation(IntFlag):
    NONE   = 0
    LOWER  = 1 << 0
    HIGHER = 1 << 1
    EQUAL  = 1 << 2
    ABOVE  = 1 << 3
    BELOW  = 1 << 4
    ZERO   = 1 << 5
    NON    = 1 << 6

class Execution(IntFlag):
    NONE   = 0
    JUMP   = 1 << 0
    RETURN = 1 << 1
    GET    = 1 << 2
    PUT    = 1 << 3
    CALL   = 1 << 4
    RET    = 1 << 5

class Memory(IntFlag):
    NONE    = 0
    NOP     = 1 << 0
    DROP    = 1 << 1
    ALLOC   = 1 << 2
    DEALLOC = 1 << 3
    PUSH    = 1 << 4
    POP     = 1 << 5
    INGEST  = 1 << 6
    REMOVE  = 1 << 7

class Validate(IntFlag):
    NOP = 0
    CMP = 1 << 0
    NOT = 1 << 1

# ==============================================================================
# 2. LIFECYCLE, PERMISSIONS & RESOURCE STATE (8-BIT BYTE BINDINGS)
# ==============================================================================

class Grants(IntFlag):
    NONE   = 0
    NO     = 1 << 0
    YES    = 1 << 1
    REJECT = 1 << 2
    ACCEPT = 1 << 3
    DROP   = 1 << 4
    TAKE   = 1 << 5
    DENY   = 1 << 6
    GRANT  = 1 << 7

class Permissions(IntFlag):
    NONE   = 0
    CREATE = 1 << 0
    READ   = 1 << 1
    UPDATE = 1 << 2
    DELETE = 1 << 3
    WRITE  = 1 << 4
    EXTEND = 1 << 5
    EXPIRE = 1 << 6
    REVOKE = 1 << 7

class Lifecycle(IntFlag):
    NONE   = 0
    NEW    = 1 << 0
    EXISTS = 1 << 1
    UNIQUE = 1 << 2
    COPY   = 1 << 3
    MOVE   = 1 << 4
    OPEN   = 1 << 5
    CLOSE  = 1 << 6

class Controls(IntFlag):
    NONE    = 0
    SKIP    = 1 << 0
    NEXT    = 1 << 1
    REWIND  = 1 << 2
    FORWARD = 1 << 3
    PLAY    = 1 << 4
    STOP    = 1 << 5
    RESTART = 1 << 6
    RESET   = 1 << 7

class Status(IntFlag):
    NONE   = 0
    OPEN   = 1 << 0
    CLOSED = 1 << 1
    INIT   = 1 << 2
    IDLE   = 1 << 3
    BUSY   = 1 << 4

class Response(IntFlag):
    NONE     = 0
    OK       = 1 << 0
    ERROR    = 1 << 1
    CRITICAL = 1 << 2
    SIGNAL   = 1 << 3

# ==============================================================================
# 3. SPATIO-TEMPORAL CONTEXT & POLICY REGISTERS (16-BIT WORD BINDINGS)
# ==============================================================================

class Times(IntFlag):
    NONE    = 0
    PAST    = 1 << 0
    FUTURE  = 1 << 1
    EARLY   = 1 << 2
    LATE    = 1 << 3
    ALWAYS  = 1 << 4
    NEVER   = 1 << 5
    PRESENT = 1 << 6
    AT      = 1 << 7
    PASSED  = 1 << 8
    YOUNGER = 1 << 9
    OLDER   = 1 << 10

class Position(IntFlag):
    NONE    = 0
    BEGIN   = 1 << 0
    END     = 1 << 1
    START   = 1 << 2
    STOP    = 1 << 3
    FAR     = 1 << 4
    CLOSEBY = 1 << 5
    HERE    = 1 << 6
    THERE   = 1 << 7

class State(IntFlag):
    NONE     = 0
    NEAR     = 1 << 0
    FAR      = 1 << 1
    FREE     = 1 << 2
    DETAINED = 1 << 3
    BUSY     = 1 << 4
    DEFLECT  = 1 << 5
    ATTRACT  = 1 << 6

class Kinetic(IntFlag):
    NONE     = 0
    INTERNAL = 1 << 0
    EXTERNAL = 1 << 1
    INSIDE   = 1 << 2
    OUTSIDE  = 1 << 3
    INNER    = 1 << 4
    OUTER    = 1 << 5
    CORE     = 1 << 6
    LAYER    = 1 << 7
    INWARDS  = 1 << 8
    OUTWARDS = 1 << 9

class Age(IntFlag):
    NONE  = 0
    YOUNG = 1 << 0
    OLD   = 1 << 1
    FRESH = 1 << 2
    STALE = 1 << 3
    NEW   = 1 << 4
    EXIST = 1 << 5

class Weights(IntFlag):
    NONE      = 0
    LESSER    = 1 << 0
    BIGGER    = 1 << 1
    MINIMAL   = 1 << 2
    MAXIMAL   = 1 << 3
    LIGHT     = 1 << 4
    HEAVY     = 1 << 5
    ESTIMATED = 1 << 6  # Derived from *_EST
    MODIFIER  = 1 << 7  # Derived from *_ER
    DOWNSIZE  = 1 << 8
    SCALE     = 1 << 9

class Policy(IntFlag):
    NONE      = 0
    ASK       = 1 << 0
    DEMAND    = 1 << 1
    RECOMMEND = 1 << 2
    REQUIRE   = 1 << 3
    POLICY    = 1 << 4
    BOUNDS    = 1 << 5
    LIMIT     = 1 << 6
    GRANT     = 1 << 7
    AVOID     = 1 << 8
    PRELUDE   = 1 << 9
    INTRO     = 1 << 10
    OUTRO     = 1 << 11
    ABSOLUTE  = 1 << 12

# ==============================================================================
# 4. DATA TYPES & METADATA LAYOUTS (16-BIT WORD BINDINGS)
# ==============================================================================

class Grouping(IntFlag):
    NONE     = 0
    SINGLE   = 1 << 0
    MULTIPLE = 1 << 1
    SOLO     = 1 << 2
    DUO      = 1 << 3
    SELECT   = 1 << 4
    CHAIN    = 1 << 5
    AT_START = 1 << 6
    AT_END   = 1 << 7

class Store(IntFlag):
    NONE      = 0
    KEY       = 1 << 0
    VALUE     = 1 << 1
    FIELD     = 1 << 2
    RESULT    = 1 << 3
    SELECT    = 1 << 4
    STRUCTURE = 1 << 5

class Type(IntFlag):
    NONE       = 0
    ALPHA      = 1 << 0
    NUMERIC    = 1 << 1
    SINGLE     = 1 << 2
    MULTIPLE   = 1 << 3
    LIST       = 1 << 4
    DICT       = 1 << 5
    OBJECT     = 1 << 6
    COLLECTION = 1 << 7

class Integrity(IntFlag):
    NONE      = 0
    EXACT     = 1 << 0
    VERIFY    = 1 << 1
    AUDIT     = 1 << 2
    HASHED    = 1 << 3
    TSTAMPED  = 1 << 4
    NOTARIZED = 1 << 5
    PUBLISHED = 1 << 6

class Crypto(IntFlag):
    NONE     = 0
    WITH     = 1 << 0
    TIMSTAMP = 1 << 1
    LOCATION = 1 << 2
    IDENTITY = 1 << 3
    WITNESS  = 1 << 4
    SIGNED   = 1 << 5
    PRIVATE  = 1 << 6
    WITHOUT  = 1 << 7
    EXTRACT  = 1 << 8
    INJECT   = 1 << 9

class Amount(IntFlag):
    NONE = 0
    A1   = 1 << 0
    A2   = 1 << 1
    A4   = 1 << 2
    A8   = 1 << 3
    A16  = 1 << 4
    A32  = 1 << 5
    A64  = 1 << 6
    A128 = 1 << 7

class Quantify(IntFlag):
    NONE   = 0
    Q1     = 1 << 0
    Q2     = 1 << 1
    Q3     = 1 << 2
    Q5     = 1 << 3
    Q10    = 1 << 4
    Q100   = 1 << 5
    Q1000  = 1 << 6
    Q10000 = 1 << 7

class Datasize(IntFlag):
    NONE    = 0
    BOOL    = 1 << 0
    NIBBLE  = 1 << 1
    BYTE    = 1 << 2
    WORD    = 1 << 3
    DOUBLE  = 1 << 4
    DYNAMIC = 1 << 5
    ARRAY   = 1 << 6

# ==============================================================================
# 5. NETWORKING TELEMETRY BINDINGS (32-BIT DUAL-REGISTERS)
# ==============================================================================

class Boundary(IntFlag):
    NONE   = 0
    SRC    = 1 << 0
    DST    = 1 << 1
    SOURCE = 1 << 2
    TARGET = 1 << 3
    ORIGIN = 1 << 4

class SourceTargetNet(IntFlag):
    NONE   = 0
    IP     = 1 << 0
    RANGE  = 1 << 1
    ASN    = 1 << 2
    ORG    = 1 << 3
    MEDIUM = 1 << 4
